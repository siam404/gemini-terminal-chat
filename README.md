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


### 1. Clone the Repository

```bash
git clone https://github.com/siam404/terminal-gemini.git
cd terminal-gemini
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env`

Create a `.env` file and add your Gemini API key like so:

```env
GEMINI_API_KEY=your_api_key_here
```

## 📁 Final Project Structure

```
terminal-gemini/
├── gemini.py           # Main script
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (e.g., API key)
└── venv/               # Python virtual environment
```


## 🚀 Make It Globally Accessible


### 1. Make the Script Executable

```bash
chmod +x gemini.py
```

### 2. Create a Symlink

```bash
mkdir -p ~/.local/bin
ln -s /home/sam/Documents/terminal-gemini/gemini.py ~/.local/bin/gemini
```

### 3. Add to Your PATH (if not already)

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## ✅ Usage

Now you can run the chatbot from **anywhere** in your terminal with:

```bash
gemini
```
No need to activate the virtual environment manually!

1. After starting the application, you'll be prompted to select a model:
   - 1: Gemini 2.5 Pro (experimental)
   - 2: Gemini 2.0 Flash
   - 3: Gemini 1.5 Flash

2. Start chatting! Type your message and press Enter to send.

3. Support multiline paste without any errors

4. To exit the chat, type `exit` or `quit`.


## 📄 License

MIT License — use freely, modify, and improve.

## ✨ Author

Made by **Ahmed Sam**  
🛠️ Terminal wizard, Python tinkerer, and AI explorer

## Acknowledgements

- Google Generative AI for providing the Gemini API
- Colorama for terminal coloring 
