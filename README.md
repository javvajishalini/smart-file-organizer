# Smart File Organizer

A Python desktop utility that automatically organizes files into categorized folders based on their file extensions. The application provides a simple folder selection dialog and intelligently sorts files while handling duplicate filenames.

## Features

* Organizes files based on their extensions
* Graphical folder selection using Tkinter
* Automatically creates destination folders
* Handles duplicate filenames safely
* Categorizes unknown file types into an `Others` folder
* Removes empty folders after organization
* Supports multiple file categories
* Displays operation status in the console

## Supported Categories

| Category      | Extensions                |
| ------------- | ------------------------- |
| TextFiles     | .txt                      |
| Documents     | .pdf, .doc, .docx         |
| Presentations | .ppt, .pptx               |
| Spreadsheets  | .xls, .xlsx, .csv         |
| Images        | .jpg, .png                |
| Videos        | .mp4                      |
| Audio         | .mp3                      |
| Archives      | .zip                      |
| Others        | Any unsupported file type |

## Technologies Used

* Python
* OS Module
* Shutil Module
* Tkinter
* File Handling

## How It Works

1. Launch the application.
2. Select a folder using the file browser dialog.
3. The program scans all files in the selected folder.
4. Files are grouped according to their extensions.
5. Required folders are created automatically.
6. Files are moved to their respective folders.
7. Empty folders are removed after organization.

## Duplicate File Handling

If a file with the same name already exists in the destination folder, the application automatically renames the new file.

Example:

Before:

photo.jpg

photo.jpg

After:

photo.jpg

photo_1.jpg

This prevents accidental overwriting of files.

## Example

### Before Organization

Downloads/

├── photo.jpg

├── resume.pdf

├── song.mp3

├── report.xlsx

├── archive.zip

### After Organization

Downloads/

├── Images/

│   └── photo.jpg

├── Documents/

│   └── resume.pdf

├── Audio/

│   └── song.mp3

├── Spreadsheets/

│   └── report.xlsx

├── Archives/

│   └── archive.zip

## Project Structure

smart-file-organizer/

├── organizer.py

├── README.md

└── screenshots/

## Future Improvements

* Drag and drop support
* Dark mode GUI
* Custom file category configuration
* Real-time folder monitoring
* Logging to a file
* Undo last organization operation

## Learning Outcomes

This project demonstrates:

* Python file handling
* Directory traversal
* GUI development with Tkinter
* Exception handling
* File system automation
* Data structures (dictionaries and sets)
* Path manipulation using the OS module
