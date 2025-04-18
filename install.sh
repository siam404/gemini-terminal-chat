#!/bin/bash

# Get the absolute path to the directory containing this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Installing Gemini Terminal Chat system-wide..."

# Create the symlink in /usr/local/bin
if [ -w /usr/local/bin ]; then
    # User has write permission to /usr/local/bin
    ln -sf "$SCRIPT_DIR/run.sh" /usr/local/bin/gemini-chat
    echo "Installation successful! You can now run 'gemini-chat' from anywhere."
else
    # User doesn't have write permission, use sudo
    echo "This installation requires administrator privileges to create a symlink in /usr/local/bin."
    sudo ln -sf "$SCRIPT_DIR/run.sh" /usr/local/bin/gemini-chat
    
    if [ $? -eq 0 ]; then
        echo "Installation successful! You can now run 'gemini-chat' from anywhere."
    else
        echo "Installation failed. Please try running this script with sudo."
        exit 1
    fi
fi

# Make sure the run.sh script is executable
chmod +x "$SCRIPT_DIR/run.sh"

echo "Done!" 