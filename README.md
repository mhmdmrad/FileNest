
# FileNest 

FileNest is a Python utility that organizes any folder by placing each file into a folder with the same name (without extension).  
This creates a clean and structured directory layout.


## How It Works
- For every file in the selected directory, a folder is created using the file name.
- The file is moved into that folder.
- Existing folders are skipped.
- Only files in the top-level directory are processed.

## Running the Program
Run the script:

    python filenest.py

You will be asked to enter a folder path.

## Entering Paths on Windows
Windows paths need special formatting. Use one of these:

Raw string:  
r"C:\Users\User\Desktop\folder"

Double backslashes:  
C:\\Users\\User\\Desktop\\folder

Forward slashes:  
C:/Users/User/Desktop/folder

Terminal input (quotes not required):  
C:\Users\User\Desktop\folder

## Requirements
- Python 3.6 or newer
