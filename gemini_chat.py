#!/usr/bin/env python3

import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Available models
MODELS = {
    "1": "gemini-2.5-pro-exp-03-25",
    "2": "gemini-2.0-flash",
    "3": "gemini-1.5-flash"
}

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
        # Try to list available models as a verification step
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
    print("1. Gemini 2.5 Pro")
    print("2. Gemini 2.0 Flash")
    print("3. Gemini 1.5 Flash")
    
    while True:
        choice = input("\nSelect a model (1-3): ")
        if choice in MODELS:
            return MODELS[choice]
        print("Invalid choice. Please select 1, 2, or 3.")

def chat(model_name, api_key):
    """Start chat session with selected model"""
    request_count = 0
    try:
        # Configure Gemini with the API key
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel(
            model_name,
            generation_config={
                "temperature": 0.2,
                "top_p": 0.8,
                "top_k": 40,
            },
            safety_settings=[
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_NONE",
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_NONE",
                },
            ],
        )
        
        # Set system instruction for direct responses
        chat = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": ["You are a direct and concise AI assistant. Answer questions directly without any extra explanations or pleasantries. Just give the answer."]
                },
                {
                    "role": "model",
                    "parts": ["Understood. I will provide direct answers without extra talk."]
                }
            ]
        )
        
        print("\nChat started! Type 'exit' or 'quit' to end the conversation.")
        print("=" * 50)
        
        while True:
            user_input = input("> ")
            if user_input.lower() in ['exit', 'quit']:
                print("\nGoodbye! Thanks for chatting.")
                break
                
            try:
                request_count += 1
                # Reconfigure API key before each message to ensure it's still valid
                genai.configure(api_key=api_key)
                response = chat.send_message(user_input)
                print(response.text)
            except Exception as e:
                error_msg = str(e)
                if "API_KEY_INVALID" in error_msg or "API key expired" in error_msg:
                    print(f"Error: API key became invalid after {request_count} requests. This might be due to:")
                    print("1. API key quota/rate limit reached")
                    print("2. API key expiration")
                    print("3. API key being revoked")
                    print("\nPlease get a new API key from https://makersuite.google.com/app/apikey")
                    return
                print(f"Error: {error_msg}")
    except Exception as e:
        print(f"Error initializing chat: {str(e)}")

def main():
    # Check if API key exists
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
    
    # Configure Gemini
    genai.configure(api_key=api_key)
    
    # Select model and start chat
    selected_model = select_model()
    chat(selected_model, api_key)

if __name__ == "__main__":
    main() 