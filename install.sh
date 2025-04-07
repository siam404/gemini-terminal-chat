#!/bin/bash

# Exit on error
set -e

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (use sudo)"
  exit 1
fi

echo "==== Installing Gemini Terminal Chat ===="

# Check if the executable exists
if [ ! -f "./dist/gemini_chat" ]; then
  echo "Executable not found. Building it now..."
  ./build.sh
fi

# Copy the executable to /usr/local/bin
echo "Installing to /usr/local/bin/gemini"
cp ./dist/gemini_chat /usr/local/bin/gemini
chmod +x /usr/local/bin/gemini

echo "==== Installation complete! ===="
echo "You can now run 'gemini' from anywhere in your terminal." 