import openai
import os
from dotenv import load_dotenv
from typing import List, Dict

# Load environment variables from .env file
load_dotenv()

# Get API key securely from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise EnvironmentError("Missing OPEN_API_KEY in .env file")

# Create OpenAI client
client = openai.OpenAI(api_key=api_key)

# Store Conversation
conversation: List[Dict[str,str]] = []

def ask_chatgpt(prompt: str) -> str:
    conversation.append({"role":"user","content": prompt})
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=conversation 
        )
        reply = response.choices[0].message.content.strip()
        conversation.append({"role":"assistant","content":reply})
        return reply
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to ChatGPT Terminal (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        reply = ask_chatgpt(user_input)
        # print("\n" + "-" * 50)
        print(f"\nAI Assistant: {reply}\n")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
