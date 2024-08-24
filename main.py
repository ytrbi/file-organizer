import subprocess
import os
from pathlib import Path
import shutil
from data import extensions

# Path to the shell script
script_path = './script.sh'

# Run the shell script
def run_shell_script(script_path):
    try:
        result = subprocess.run(['bash', script_path], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")
        print(f"Script output: {e.output}")

def organize_files(source_dir, dest_dir):
    # Convert to absolute paths for clarity
    source_dir = Path(source_dir).resolve()
    dest_dir = Path(dest_dir).resolve()
    
    print(f"Source directory: {source_dir}")
    print(f"Destination directory: {dest_dir}")

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")
    if not dest_dir.exists():
        os.makedirs(dest_dir)

    # List all files in the source directory
    files = os.listdir(source_dir)
    # Set to track which extension categories are present
    present_categories = set()

    # Determine which categories are present in the directory
    for file in files:
        if os.path.isfile(source_dir / file):
            file_extension = file.split('.')[-1]
            if file_extension in extensions:
                present_categories.add(extensions[file_extension])

    # Create the necessary subfolders based on present categories
    for category in present_categories:
        folder_path = dest_dir / category
        os.makedirs(folder_path, exist_ok=True)
    
    # Organize files by moving them to appropriate folders
    for file in files:
        if os.path.isfile(source_dir / file):
            file_extension = file.split('.')[-1]
            if file_extension in extensions:
                category = extensions[file_extension]
                src_path = source_dir / file
                dest_path = dest_dir / category / file
                try:
                    shutil.move(src_path, dest_path)
                    print(f"Moved {file} to {dest_path}")
                except Exception as e:
                    print(f"Error moving {file}: {e}")

def main():
    run_shell_script(script_path)
    source_dir = '/Users/ya/Desktop/python/practice/files/dummy-files'  # Use absolute path
    dest_dir = '/Users/ya/Desktop/python/practice/files/organized_files'  # Use absolute path
    organize_files(source_dir, dest_dir)

main()
