#!/usr/bin/env python3

import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv
import json
from colorama import Fore, Style, init
import time

# Initialize colorama
init()

# Load environment variables
load_dotenv()

# Available models
MODELS = {
    "1": "gemini-2.5-pro-exp-03-25",
    "2": "gemini-2.0-flash",
    "3": "gemini-1.5-flash"
}

# Fixed sparkles icon for AI responses
AI_ICON = "✨"

def save_api_key(api_key):
    """Save API key to .env file"""
    with open('.env', 'w') as f:
        f.write(f'GOOGLE_API_KEY={api_key}')

def load_api_key():
    """Load API key from .env file"""
    return os.getenv('GOOGLE_API_KEY')

def verify_api_key(api_key):
    """Verify if the API key is valid"""
    try:
        genai.configure(api_key=api_key)
        models = genai.list_models()
        if not models:
            return False, "No models available"
        return True, None
    except Exception as e:
        error_msg = str(e)
        if "API_KEY_INVALID" in error_msg or "API key expired" in error_msg:
            return False, "API key is invalid or expired. Please get a new API key from https://makersuite.google.com/app/apikey"
        return False, f"Error verifying API key: {error_msg}"

def select_model():
    """Let user select a model"""
    print("\nAvailable models:")
    for key, model in MODELS.items():
        model_name = model.split("-")
        if len(model_name) >= 3:
            version = f"{model_name[1]} {model_name[2].capitalize()}"
            if len(model_name) >= 4 and model_name[3] == "exp":
                version += " (Experimental)"
        else:
            version = model
        print(f"{key}. Gemini {version}")
    
    while True:
        choice = input("\nSelect a model (1-3): ")
        if choice in MODELS:
            return MODELS[choice]
        print("Invalid choice. Please select 1, 2, or 3.")

def get_input(prompt=""):
    """Enhanced input function that handles multiline pastes silently"""
    if prompt:
        print(prompt, end="", flush=True)
    
    # First try to get input normally - this works for most cases
    # and doesn't interfere with normal typing behavior
    try:
        line = input()
        
        # Check if this might be the start of a multiline paste
        # (when pasting, all content comes immediately)
        if sys.stdin.isatty():
            import select
            # Check if there's immediately more input waiting
            rlist, _, _ = select.select([sys.stdin], [], [], 0.001)
            if not rlist:
                # No more input waiting - this was a normal single-line input
                return line
                
            # There's more input waiting, likely a paste - collect it
            lines = [line]
            while True:
                rlist, _, _ = select.select([sys.stdin], [], [], 0.001)
                if not rlist:
                    break
                    
                try:
                    next_line = input()
                    lines.append(next_line)
                except EOFError:
                    break
                    
            return '\n'.join(lines)
        else:
            # Non-TTY input (e.g., redirected from a file)
            return line
            
    except Exception:
        # Fallback to basic input if anything goes wrong
        return input()

def chat(model_name, api_key):
    """Start chat session with selected model"""
    request_count = 0
    try:
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel(
            model_name,
            generation_config={
                "temperature": 0.2,
                "top_p": 0.8,
                "top_k": 40,
            },
            safety_settings=[
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
            ],
        )
        
        chat = model.start_chat(
            history=[
                {"role": "user", "parts": ["You are a direct and concise AI assistant. Answer questions directly without any extra explanations or pleasantries. Just give the answer."]},
                {"role": "model", "parts": ["Understood. I will provide direct answers without extra talk."]}
            ]
        )
        
        print("\nChat started! Type 'exit' or 'quit' to end the conversation.")
        print("-" * 60)
        
        while True:
            # Get user input and handle paste detection automatically
            try:
                user_input = get_input("> ")
            except Exception as e:
                # Fall back to regular input if the advanced method fails
                print("> ", end="", flush=True)
                user_input = input()
            
            # Check for exit command
            if user_input.lower() in ['exit', 'quit']:
                print("\nGoodbye! Thanks for chatting.")
                break
                
            # Handle explicit multiline input markers
            if user_input.strip() == '<multiline>':
                print("Enter your multiline input (type '</multiline>' on a new line when done):")
                lines = []
                while True:
                    line = input()
                    if line.strip() == '</multiline>':
                        break
                    lines.append(line)
                user_input = '\n'.join(lines)
            
            # Handle triple backticks
            elif user_input.strip() == '```':
                print("Paste your multiline content (end with ``` on a new line):")
                lines = []
                while True:
                    line = input()
                    if line.strip() == '```':
                        break
                    lines.append(line)
                user_input = '\n'.join(lines)
            
            # Skip if empty
            if not user_input.strip():
                print("Error: Content must not be empty. Please enter some text.")
                continue
                
            try:
                request_count += 1
                genai.configure(api_key=api_key)
                response = chat.send_message(user_input)
                print(f"{AI_ICON} {Fore.CYAN}{response.text}{Style.RESET_ALL}")
            except Exception as e:
                error_msg = str(e)
                if "API_KEY_INVALID" in error_msg or "API key expired" in error_msg:
                    print(f"Error: API key became invalid after {request_count} requests. This might be due to:")
                    print("1. API key quota/rate limit reached")
                    print("2. API key expiration")
                    print("3. API key being revoked")
                    print("\nPlease get a new API key from https://makersuite.google.com/app/apikey")
                    return
                elif "content must not be empty" in error_msg.lower():
                    print("Error: Content must not be empty. Please enter some text.")
                else:
                    print(f"Error: {error_msg}")
    except Exception as e:
        print(f"Error initializing chat: {str(e)}")

def main():
    api_key = load_api_key()
    
    if not api_key:
        print("No API key found. Please set your Google API key.")
        api_key = input("Enter your Google API key: ")
        
        is_valid, error_msg = verify_api_key(api_key)
        if is_valid:
            save_api_key(api_key)
            print("API key verified and saved successfully!")
        else:
            print(error_msg)
            sys.exit(1)
    else:
        is_valid, error_msg = verify_api_key(api_key)
        if not is_valid:
            print(error_msg)
            api_key = input("Enter your Google API key: ")
            
            is_valid, error_msg = verify_api_key(api_key)
            if is_valid:
                save_api_key(api_key)
                print("API key verified and saved successfully!")
            else:
                print(error_msg)
                sys.exit(1)
    
    genai.configure(api_key=api_key)
    
    selected_model = select_model()
    chat(selected_model, api_key)

if __name__ == "__main__":
    main()

