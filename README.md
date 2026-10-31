# Automatic File Organizer 

A simple Python command-line application that automatically organizes files into separate folders based on their file extensions.

It helps keep folders clean and organized by sorting files into categories such as Images, Documents, Videos, Audio, Archives, and Code.

## Features

Automatically organizes files by file type.

Supports multiple file extensions.

Creates category folders automatically.

Skips files if a file with the same name already exists in the destination folder.

Includes a dry-run option to preview changes without moving files.

Uses Python's built-in libraries.


## How to Run

1. Clone the repository
2. Navigate to the project folder
3. Run the program

python organizer.py 

Replace the example folder path with the folder you want to organize.


##Preview Changes (Dry Run)

To see which files would be moved without actually moving them, use:

python organizer.py "C:/Users/YourName/Downloads" --dry-run

This displays the planned changes without modifying the folder.

## Example Output

photo.jpg -> Images/
report.pdf -> Documents/
song.mp3 -> Audio/
project.py -> Code/
movie.mp4 -> Videos/

Moved 5 file(s).
