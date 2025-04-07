# Gemini Terminal Chat

![Gemini Terminal Chat](https://img.shields.io/badge/Gemini-Terminal%20Chat-blue)
![License](https://img.shields.io/github/license/YOUR_USERNAME/gemini-terminal-chat)

A simple terminal-based chat application that allows you to interact with Google's Gemini AI models directly from your terminal.

![Demo](demo.gif)

## Features

- 🤖 Chat with Google's Gemini AI models directly from your terminal
- 🚀 Support for multiple Gemini models (2.5 Pro, 2.0 Flash, 1.5 Flash)
- 🎯 Direct-to-the-point AI responses
- 🔒 Secure API key storage
- 🧠 Simple and intuitive interface

## Prerequisites

- A Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Linux/macOS system (Windows support via WSL)

## Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/siam404/gemini-terminal-chat.git
   cd gemini-terminal-chat
   ```

2. Run the application:
   ```bash
   ./run.sh
   ```

## Available Installation Methods

- **Pre-built executable**: Just run `./run.sh`
- **System-wide installation**: Run `sudo ./install.sh`
- **User-level alias**: Run `./setup-alias.sh`
- **Build from source**: Run `./build.sh`
- **Manual Python setup**: Install dependencies and run with Python

For detailed instructions, see the [full installation process](Installation.md).

## Usage

1. When you first run the program, you'll be asked to enter your Google API key
2. Select the model you want to use
3. Start chatting!
4. Type 'exit' or 'quit' to end the conversation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Google Gemini API
- PyInstaller for creating the standalone executable 
