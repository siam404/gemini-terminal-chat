# Gemini Terminal Chat

A simple and powerful terminal-based chat application that uses Google's Gemini AI models. Chat with Gemini directly from your terminal with support for multiple models including Gemini 1.5, 2.0, and 2.5.

![Demo](demo.gif)

## Features

- Clean terminal interface for chatting with Gemini AI
- Support for multiple Gemini models (1.5 Flash, 2.0 Flash, 2.5 Pro)
- Handles multiline input for code and long text
- Automatically saves your API key for future sessions
- Colorized output for better readability

## Installation

### Prerequisites

- Python 3.6 or higher
- A Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Quick Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/gemini-terminal-chat.git
   cd gemini-terminal-chat
   ```

2. Make the run script executable:
   ```bash
   chmod +x run.sh
   ```

3. Run the application:
   ```bash
   ./run.sh
   ```

The script will:
- Ask for your Google API key on first run
- Create a virtual environment automatically
- Install required dependencies
- Launch the chat application

### Manual Installation

If you prefer to set things up manually:

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API key:
   ```bash
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```

4. Run the application:
   ```bash
   python gemini.py
   ```

## Usage

1. After starting the application, you'll be prompted to select a model:
   - 1: Gemini 2.5 Pro (experimental)
   - 2: Gemini 2.0 Flash
   - 3: Gemini 1.5 Flash

2. Start chatting! Type your message and press Enter to send.

3. Support multiline paste without any errors

4. To exit the chat, type `exit` or `quit`.

## System-Wide Installation

To make the chat available system-wide:

```bash
# Create a symlink to the run.sh script in a directory that's in your PATH
sudo ln -s $(pwd)/run.sh /usr/local/bin/gemini-chat

# Now you can run the chat from anywhere with:
gemini-chat
```

## License

This project is open-source under the MIT License.

## Acknowledgements

- Google Generative AI for providing the Gemini API
- Colorama for terminal coloring 
