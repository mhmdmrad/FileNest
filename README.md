
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

Windows paths contain backslashes ( \ ).  
Python interprets many backslash sequences as escape characters, such as:

\u  \n  \t  \r

Because of this, writing a normal Windows path like:

"C:\Users\User\Desktop\folder"

will not work correctly.

To avoid this problem, use one of the following formats:

Raw string:  
r"C:\Users\User\Desktop\folder"

Double backslashes:  
C:\\Users\\User\\Desktop\\folder

Forward slashes:  
C:/Users/User/Desktop/folder

Terminal input without quotes:  
C:\Users\User\Desktop\folder

## Requirements
- Python 3.6 or newer
