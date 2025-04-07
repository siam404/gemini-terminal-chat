# Gemini Terminal Chat

A simple terminal-based chat application that allows you to interact with Google's Gemini AI models directly from your terminal.

## Features

- Support for multiple Gemini models:
  - Gemini 2.5 Pro
  - Gemini 2.0 Flash
  - Gemini 1.5 Flash
- Direct-to-the-point AI responses
- Secure API key storage
- Simple and intuitive interface

## Prerequisites

- Get a Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Installation

This repository includes several ways to install and run Gemini Terminal Chat:

### Option 1: Run from the pre-built executable

1. Clone this repository
2. Run the application:
   ```bash
   ./run.sh
   ```

### Option 2: Use the setup scripts

#### For system-wide installation (requires sudo):
```bash
sudo ./install.sh
```
This will make the `gemini` command available system-wide.

#### For user-level alias setup (no sudo required):
```bash
./setup-alias.sh
```
This will add an alias to your `~/.bashrc` file. Remember to run `source ~/.bashrc` or restart your terminal afterward.

### Option 3: Build from source

If you want to build the executable yourself:

1. Run the build script:
   ```bash
   ./build.sh
   ```
   This will create an executable at `dist/gemini_chat` and a symlink named `gemini` in the current directory.

2. Run the application:
   ```bash
   ./gemini
   ```

### Option 4: Manual Python setup

1. Make sure you have Python 3.7+ and pip installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python gemini_chat.py
   ```

## Usage

1. When you first run the program, you'll be asked to enter your Google API key
2. Select the model you want to use
3. Start chatting!
4. Type 'exit' or 'quit' to end the conversation

## Troubleshooting

### API Key Issues
If you encounter issues with your API key:
- Make sure you've created a valid API key at https://makersuite.google.com/app/apikey
- Check that you have quota available for the API
- Try creating a new API key if your current one isn't working

### Model Not Found
If you get "model not found" errors:
- Try using a different model
- Verify that the model is available in your region

## License

MIT License

## Acknowledgments

- Google Gemini API
