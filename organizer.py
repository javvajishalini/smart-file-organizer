import os
import shutil

def organize_files(directory):
    # Check if the folder exists
    if not os.path.exists(directory):
        print("Error: The folder you entered does not exist.")
        return

    # A simple dictionary to map file extensions to folder names
    extensions_map = {
        '.txt': 'TextFiles',
        '.pdf': 'Documents',
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.xls': 'Spreadsheets',
        '.xlsx': 'Spreadsheets',
        '.csv': 'Spreadsheets',
        '.jpg': 'Images',
        '.png': 'Images',
        '.mp4': 'Videos',
        '.mp3': 'Audio',
        '.zip': 'Archives'
    }

    files_moved = 0
    
    # Loop through every file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # We only want to organize files, not folders
        if os.path.isdir(file_path):
            continue

        # Get the file's extension (like .txt, .jpg)
        name, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Decide which folder the file belongs to, default to 'Others'
        if ext in extensions_map:
            folder_name = extensions_map[ext]
        else:
            folder_name = 'Others'
            
        folder_path = os.path.join(directory, folder_name)

        # Create the folder if it's not already there
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Build the final destination path
        destination = os.path.join(folder_path, filename)
        
        # If a file with the exact same name already exists in the folder, change the name slightly
        counter = 1
        while os.path.exists(destination):
            new_filename = f"{name}_{counter}{ext}"
            destination = os.path.join(folder_path, new_filename)
            counter += 1

        # Move the file into the new folder
        shutil.move(file_path, destination)
        print(f"Moved: {filename} -> {folder_name}")
        files_moved += 1
        
    print(f"\nAll done! Successfully moved {files_moved} files.")

if __name__ == "__main__":
    print("=== Smart File Organizer ===")
    target_dir = input("Enter the path of the folder you want to organize: ")
    organize_files(target_dir)
