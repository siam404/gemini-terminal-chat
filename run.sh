#!/bin/bash

# Configuration variables
CONFIG_DIR="$HOME/.config/gemini-chat"
API_KEY_FILE="$CONFIG_DIR/api_key.env"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create configuration directory if it doesn't exist
mkdir -p "$CONFIG_DIR"

# Check if API key exists in the config directory
if [ ! -f "$API_KEY_FILE" ]; then
    echo "No API key found. You'll need a Google API key to use this application."
    echo "Get your API key from https://makersuite.google.com/app/apikey"
    read -p "Enter your Google API key: " API_KEY
    
    # Save API key to config file
    echo "GOOGLE_API_KEY=$API_KEY" > "$API_KEY_FILE"
    echo "API key saved successfully!"
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "$SCRIPT_DIR/venv" ]; then
    echo "Setting up virtual environment..."
    python3 -m venv "$SCRIPT_DIR/venv"
fi

# Activate virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

# Install requirements if needed
if [ ! -f "$SCRIPT_DIR/.requirements_installed" ]; then
    echo "Installing requirements..."
    pip install -r "$SCRIPT_DIR/requirements.txt"
    touch "$SCRIPT_DIR/.requirements_installed"
fi

# Copy API key to local .env for the application
cp "$API_KEY_FILE" "$SCRIPT_DIR/.env"

# Run the application
python "$SCRIPT_DIR/gemini.py" 