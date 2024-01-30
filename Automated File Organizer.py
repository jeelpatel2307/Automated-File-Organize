# automated_file_organizer.py

import os
import shutil

def organize_files(source_dir, destination_dir):
    """
    Organize files in the source directory into separate folders based on their file types.

    Args:
    - source_dir (str): Path to the source directory containing files to be organized.
    - destination_dir (str): Path to the destination directory where organized folders will be created.
    """
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get a list of all files in the source directory
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    for file in files:
        # Get the file extension
        _, file_extension = os.path.splitext(file)

        # Create a folder for the file type if it doesn't exist
        file_type_folder = os.path.join(destination_dir, file_extension[1:].lower())
        if not os.path.exists(file_type_folder):
            os.makedirs(file_type_folder)

        # Move the file to the corresponding folder
        source_file_path = os.path.join(source_dir, file)
        destination_file_path = os.path.join(file_type_folder, file)
        shutil.move(source_file_path, destination_file_path)

if __name__ == "__main__":
    source_directory = input("Enter the path to the source directory: ")
    destination_directory = input("Enter the path to the destination directory: ")

    organize_files(source_directory, destination_directory)
    print("Files organized successfully!")
