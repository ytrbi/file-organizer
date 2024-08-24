import subprocess
import os
from pathlib import Path
import shutil
from data import extensions

# Path to the shell script
script_path = './script.sh'

# Run the shell script
# def run_shell_script(script_path):
#     try:
#         result = subprocess.run(['bash', script_path], check=True, capture_output=True, text=True)
#         print(result.stdout)
#     except subprocess.CalledProcessError as e:
#         print(f"Error running script: {e}")
#         print(f"Script output: {e.output}")

def scan_directory(source_dir):
    # Return a list of file paths in the directory
    file_list = []
    for item in os.listdir(source_dir):
        file_path = os.path.join(source_dir, item)
        if os.path.isfile(file_path):
            file_list.append(file_path)
    return file_list

def create_subfolders(source_dir, file_list):
    # Create folders based on file extensions
    present_categories = set()
    
    for file_path in file_list:
        _, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.lstrip('.').lower()
        if file_extension in extensions:
            folder_name = extensions[file_extension]
            present_categories.add(folder_name)
    
    # Create the folders
    for category in present_categories:
        folder_path = os.path.join(source_dir, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

def move_files_to_folder(source_dir, file_list):
    for file in file_list:
        _, file_extension = os.path.splitext(file)
        file_extension = file_extension.lstrip('.').lower()
        if file_extension in extensions:
            folder_name = extensions[file_extension]
            folder_path = os.path.join(source_dir, folder_name)
            shutil.move(file, folder_path)  # Move the file to the folder
            print(f"Moved {file} to {folder_path}")

def main():./
    while True:
        source_dir = input('Enter the path to be organized: ').strip()  # Get the path to be organized from the user
        
        if not os.path.isdir(source_dir):
            print(f"The directory {source_dir} does not exist. Please try again.")
            continue  # Ask the user to input the path again
        
        try:
            file_list = scan_directory(source_dir)
            create_subfolders(source_dir, file_list)
            move_files_to_folder(source_dir, file_list)
            print("Organization complete.")
            break  # Exit the loop after successful execution
        
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
            continue  # Ask the user to input the path again
    source_dir = input('Enter the path to be organized: ') # Get the path to be organized from the user
    
    if os.path.isdir(source_dir):
        file_list = scan_directory(source_dir)
        create_subfolders(source_dir, file_list)
        move_files_to_folder(source_dir, file_list)
    else:
        print(f"The directory {source_dir} does not exist.")

if __name__ == "__main__":
    main()
