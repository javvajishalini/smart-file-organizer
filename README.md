# Smart File Organizer

A simple Python script to automatically organize files in a directory into subfolders based on their file extensions.

## Features
- Organizes `.txt`, `.pdf`, `.jpg`, `.png`, `.mp4`, `.mp3`, `.zip`, `.csv`, `.pptx`, and more into respective folders.
- Any unmapped extensions are moved into an `Others` folder.
- Prevents overwriting files with the same name.
- Handles errors gracefully when moving files.

## Usage
Run the script using python:
```bash
python organizer.py
```
You will be prompted to enter the directory you wish to organize.
