#!/bin/bash

# Check if the executable exists
if [ -f "./dist/gemini_chat" ]; then
    # Run the executable
    ./dist/gemini_chat
elif [ -f "./gemini" ]; then
    # Run the symbolic link
    ./gemini
else
    echo "Executable not found. Please run ./build.sh first to build the application."
    echo "Do you want to build the application now? (y/n)"
    read answer
    if [ "$answer" == "y" ] || [ "$answer" == "Y" ]; then
        ./build.sh
        if [ -f "./dist/gemini_chat" ]; then
            ./dist/gemini_chat
        else
            echo "Build failed. Please check the error messages above."
        fi
    else
        echo "Build cancelled. Exiting."
    fi
fi 