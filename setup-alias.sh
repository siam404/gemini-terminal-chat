#!/bin/bash

echo "==== Setting up Gemini alias ===="

# Get the absolute path to the executable
EXEC_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/dist/gemini_chat"

# Check if the executable exists
if [ ! -f "$EXEC_PATH" ]; then
  echo "Executable not found. Building it now..."
  ./build.sh
  EXEC_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/dist/gemini_chat"
fi

# Add the alias to .bashrc if it doesn't exist already
if ! grep -q "alias gemini=" ~/.bashrc; then
  echo "# Gemini Terminal Chat alias" >> ~/.bashrc
  echo "alias gemini='$EXEC_PATH'" >> ~/.bashrc
  echo "Alias added to ~/.bashrc"
  echo "Please run 'source ~/.bashrc' or restart your terminal to use the 'gemini' command."
else
  echo "Alias already exists in ~/.bashrc"
  echo "You can use the 'gemini' command after running 'source ~/.bashrc' or restarting your terminal."
fi

echo "==== Setup complete! ====" 