import os
from threading import Thread
import time

class FileManager:
    def __init__(self, input='input', output='output', time_interval=3):
        self.input = input
        self.output = output
        self.time_interval = time_interval
        self.file_handler = {
            'PacketI': self.integer_packet,
            'PacketC': self.char_packet
        }

    def process_files(self):
        while True:
            print(f"Checking directory: {self.input}") 
            filenames = os.listdir(self.input)
            print(f"Files found: {filenames}")
            for filename in os.listdir(self.input):
                filepath = os.path.join(self.input, filename)
                if os.path.isfile(filepath):
                    try:
                        handler = self.get_packet_handler(filename)
                        if handler:
                            handler(filepath)
                    except Exception as e:
                        print(f"Error processing {filename}: {e}")
                    finally:
                        os.remove(filepath) 
                        print(f"File : {filename} removed ")
            time.sleep(self.time_interval)

    def get_packet_handler(self, filename):
        for packet_type, handler in self.file_handler.items():
            if packet_type in filename:
                return handler
        return None

    def integer_packet(self, filepath):
        all_lines = []
        with open(filepath, 'r') as file:
            for line in file:
                filter_unsorted_line = []
                line_to_list = list(map(int, line.split(',')))
                for num in line_to_list:
                    if not filter_unsorted_line or num >= filter_unsorted_line[-1]:
                        filter_unsorted_line.append(num)
                all_lines.extend(filter_unsorted_line)
        all_lines.sort()

        if all_lines:  
            if not os.path.exists(self.output):
                os.makedirs(self.output)
                print('output folder created')

            output_file = os.path.join(self.output, f"output_{os.path.basename(filepath)}")

            with open(output_file, 'w') as f:
                f.write(','.join(map(str, all_lines)))
            print(f"{filepath} -- sorted integer packet added to: {output_file}")
        else:
            print(f"No valid integers found in {filepath}")

    def find_longest_substrings(self, s):
        max_len = 0
        substrings = set()
        start = 0
        seen = {}

        for end, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            seen[char] = end
            current_len = end - start + 1
            if current_len > max_len:
                max_len = current_len
                substrings = {s[start:end + 1]}
            elif current_len == max_len:
                substrings.add(s[start:end + 1])

        return substrings

    def char_packet(self, filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        only_letters = ''.join(filter(str.islower, content))
        
        if only_letters:  
            longest_substring = self.find_longest_substrings(only_letters)

            if not os.path.exists(self.output):
                os.makedirs(self.output)
                print('output folder created')
            output_file = os.path.join(self.output, f"output_{os.path.basename(filepath)}")

            with open(output_file, 'w') as f:
                for substring in longest_substring:
                    f.write(f"{substring} \n")
            print(f"{filepath} -- longest substring packet added to: {output_file}")
        else:
            print(f"No lowercase letters found in {filepath}")

if __name__ == "__main__":
    files = FileManager()
    file_thread = Thread(target=files.process_files)
    file_thread.start()
