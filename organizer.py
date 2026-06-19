import os
import shutil
import argparse
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def organize_files(directory):
    """Organizes files in the given directory based on their extensions."""
    if not os.path.exists(directory):
        logging.error(f"The directory '{directory}' does not exist.")
        return

    # Extended mapping of extensions to folder names
    extensions_map = {
        '.txt': 'TextFiles',
        '.pdf': 'Documents',
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.xls': 'Spreadsheets',
        '.xlsx': 'Spreadsheets',
        '.csv': 'Spreadsheets',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.mp4': 'Videos',
        '.mkv': 'Videos',
        '.mp3': 'Audio',
        '.wav': 'Audio',
        '.zip': 'Archives',
        '.rar': 'Archives',
        '.tar': 'Archives',
        '.gz': 'Archives',
        '.py': 'CodeFiles',
        '.js': 'CodeFiles',
        '.html': 'CodeFiles',
        '.css': 'CodeFiles'
    }

    files_moved = 0
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

        # Handle filename collisions
        base_name, extension = os.path.splitext(filename)
        destination = os.path.join(folder_path, filename)
        counter = 1
        while os.path.exists(destination):
            new_filename = f"{base_name} ({counter}){extension}"
            destination = os.path.join(folder_path, new_filename)
            counter += 1

        # Move the file
        shutil.move(file_path, destination)
        logging.info(f"Moved: {filename} -> {os.path.relpath(destination, directory)}")
        files_moved += 1
        
    logging.info(f"Organization complete! Total files moved: {files_moved}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart File Organizer: Sort files into folders by extension.")
    parser.add_argument("directory", nargs="?", help="Path to the directory to organize")
    
    args = parser.parse_args()
    
    if args.directory:
        target_directory = args.directory
    else:
        target_directory = input("Enter the path of the directory to organize: ")
        
    organize_files(target_directory)
