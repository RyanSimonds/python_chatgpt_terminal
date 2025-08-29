import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key securely from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ API key not found. Make sure it's in your .env file as OPENAI_API_KEY.")
    exit(1)

# Create OpenAI client
client = openai.OpenAI(api_key=api_key)

def ask_chatgpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"

def main():
    print("💬 ChatGPT Terminal (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        reply = ask_chatgpt(user_input)
        print(f"Assistant: {reply}\n")

if __name__ == "__main__":
    main()
