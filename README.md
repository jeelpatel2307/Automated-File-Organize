# Automated File Organizer

The Automated File Organizer is a simple Python script that organizes files in a specified directory based on their file types into separate folders.

## How It Works

1. **User Input:**
    - The script prompts the user to enter the path to the source directory containing files to be organized.
    - The user also provides the path to the destination directory where organized folders will be created.
2. **Organization Process:**
    - The script retrieves a list of all files in the source directory.
    - For each file, it extracts the file extension and creates a folder for the corresponding file type in the destination directory.
3. **File Movement:**
    - The script moves each file from the source directory to the appropriate file type folder in the destination directory.

## Usage

1. **Run the Script:**
    - Save the script in a file, for example, `automated_file_organizer.py`.
    - Open a terminal or command prompt and run the script using a Python interpreter:
        
        ```bash
        python automated_file_organizer.py
        
        ```
        
2. **User Input:**
    - Enter the path to the source directory as prompted.
    - Enter the path to the destination directory.
3. **Organization:**
    - The script will organize the files based on their types into separate folders in the destination directory.

## Customization

- **File Types:**
    - Modify the script to add additional file types to the organization process.
- **Folder Structure:**
    - Customize the folder structure in the destination directory according to your preferences.
- **Subdirectories:**
    - Enhance the script to handle subdirectories within the source directory.
- **Error Handling:**
    - Add error handling and validation for user inputs to improve the robustness of the script.

Feel free to use, modify, and share this script to suit your file organization needs!

---

## Author

Jeel patel
