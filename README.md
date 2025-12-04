
# FileNest 

FileNest is a Python utility that organizes any folder by placing each file into a folder with the same name (without extension).  
This creates a clean and structured directory layout.

---

## Features
- Creates a folder for every file  
- Folder name matches file name  
- Moves the file into its corresponding folder  
- Skips existing folders  
- Works on Windows, macOS, and Linux

---

## Example

Before:

photo.png  
notes.pdf  
song.mp3  

After:

photo/photo.png  
notes/notes.pdf  
song/song.mp3  

---

## Windows Path Input

Windows paths require special formatting. Use one of the following:

-Raw string (recommended):
r"C:\Users\User\Desktop\folder"

-Double backslashes:
C:\Users\User\Desktop\folder

-Forward slashes:
C:/Users/User/Desktop/folder

-Terminal input without quotes:
C:\Users\User\Desktop\folder

## Requirements

Python 3.6+
