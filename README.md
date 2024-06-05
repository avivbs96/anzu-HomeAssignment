
# FileManager Project

## Overview

The FileManager script processes files in the specified input folder and generates output files in the output folder. It handles two types of packets:
- **Integer Packets** (files containing comma-separated integers)
- **Character Packets** (files containing lowercase letters)

## File Processing

- **Integer Packets**: 
  - The script reads the file and filters out unsorted integers.
  - It then sorts the integers and saves them to the output folder.
- **Character Packets**: 
  - The script reads the file and extracts only lowercase letters.
  - It finds the longest substrings of unique characters and saves them to the output folder.

## Running the Script

To run the script, execute the following command in your terminal:
```
python3 script.py
```

### Multithreading

The script uses the `threading` library to run the file processing function in a separate thread, allowing for continuous monitoring and processing of files in the input folder without blocking the main program.

### File Handling

The script utilizes the `os.listdir()` method to list all files in the input directory. It then processes each file based on its type (Integer Packet or Character Packet) and deletes the file from the input folder after processing.

## Important Notes

1. **Input Files Deletion**: After running the script, the input files in the `input` folder will be deleted.
2. **Output Files Creation**: After running the script, the output files will be created in the `output` folder.

## Demonstration Video

For a visual demonstration of the script running, please watch the video on [Google Drive](https://drive.google.com/file/d/1Td_C2Fhu6W8Pdj-9hfHDJfD4RO-IZJM4/view?usp=drive_link).

