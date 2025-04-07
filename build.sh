#!/bin/bash

# Exit on error
set -e

echo "==== Setting up virtual environment ===="
python3 -m venv venv
source venv/bin/activate

echo "==== Installing dependencies ===="
pip install -r requirements.txt
pip install pyinstaller

echo "==== Building executable ===="
pyinstaller --onefile gemini_chat.py

echo "==== Build complete! ===="
echo "The executable can be found in: $(pwd)/dist/gemini_chat"
echo "To run it, use: ./dist/gemini_chat"

# Create a symbolic link for easier access
ln -sf "$(pwd)/dist/gemini_chat" "$(pwd)/gemini"
echo "A symbolic link 'gemini' has been created in the current directory"
echo "You can run the program with: ./gemini" 