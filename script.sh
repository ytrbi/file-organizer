#!/bin/bash

# Create the dummy-files directory
mkdir -p './dummy-files'

# Change to the dummy-files directory
cd './dummy-files'

# '-p' attribute allows the command to create parent directories without errors

# Creating dummy files
touch report.txt
touch vacation_photo.jpg
touch resume.docx
touch code.py
touch presentation.pptx
touch data.cs
touch script.js
touch song.mp3
touch document.pdf
touch image.png
touch readme.md
touch notes.txt

echo "Test files created in $(pwd)"

#  'chmod +x script.sh ' this command has been used in the terminal to allow excution for this file without getting into trouble
