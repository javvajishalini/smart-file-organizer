import os
import shutil

def organize_files(directory):
    """Organizes files in the given directory based on their extensions."""
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Basic mapping of extensions to folder names
    extensions_map = {
        '.txt': 'TextFiles',
        '.pdf': 'Documents',
        '.jpg': 'Images',
        '.png': 'Images',
        '.mp4': 'Videos',
        '.mp3': 'Audio'
    }

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Find the folder name for the extension, or use 'Others'
        folder_name = extensions_map.get(ext, 'Others')
        folder_path = os.path.join(directory, folder_name)

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file
        destination = os.path.join(folder_path, filename)
        shutil.move(file_path, destination)
        print(f"Moved: {filename} -> {folder_name}/")

if __name__ == "__main__":
    target_directory = input("Enter the path of the directory to organize: ")
    organize_files(target_directory)
    print("Organization complete!")
