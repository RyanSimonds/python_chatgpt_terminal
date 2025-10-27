"""
ChatGPT Terminal Interface

Interactive command-line program that allows users to chat with OpenAI's
ChatGPT model (gpt-3.5-turbo). Users can input prompts, receive 
AI-generated responses, and continue the conversation in a single 
terminal session.

Features:
- Stores conversation context to maintain multi-turn dialogue
- Colored terminal output using ANSI escape codes for better readibility
- Securely loads OpenAI API key from environment variables

Functions:
- ask_chatgpt(prompt: str) -> str: 
    Sends a user prompt to ChatGPT and returns the response
- main(): 
    Runs the terminal user interface and managers the chat loop
"""


import openai
import os
from dotenv import load_dotenv
from typing import List, Dict

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"

# Load environment variables from .env file
load_dotenv()

# Get API key securely from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise EnvironmentError(f"{RED}Missing OPENAI_API_KEY in .env file{RESET}")

# Create OpenAI client
client = openai.OpenAI(api_key=api_key)

# Store Conversation
conversation: List[Dict[str,str]] = []

# ChatGPT prompt code
def ask_chatgpt(prompt: str) -> str:
    conversation.append({"role":"user","content": prompt})
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=conversation 
        )
        reply = response.choices[0].message.content.strip()
        conversation.append({"role":"assistant","content": reply})
        return reply
    except Exception as error:
        return f"{RED}Error: {error}{RESET}"


# User interface
def main():
    print(f"{BOLD}{BLUE}\nWelcome to ChatGPT Terminal{RESET} " 
          "(type 'exit' to quit)\n")
    print("-" * 50 + "\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print(f"\n{GREEN}Exiting Program. Goodbye!\n{RESET}")
            break
        
        print(f'{YELLOW}\nLoading...{RESET}')

        reply = ask_chatgpt(user_input)
        print(f"\nAI Assistant: {reply}")
        print("\n" + "-" * 50 + "\n")


# Program's entry point check
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n{GREEN}Exiting Program. Goodbye!\n{RESET}")
