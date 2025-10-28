# ChatGPT Terminal

**ChatGPT Terminal** is an interactive Python program that lets you chat with OpenAI's GPT model directly from your terminal. Users can input messages, get AI responses, and continue the conversation in a terminal-friendly interface.

## Features
- Chat with OpenAI's GPT model (GPT-3.5-turbo)
- Colored terminal output for clarity
- Easy-to-use interface with exit commands
- Secure API key usage via `.env` file
- Conversation history preserved during session

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chatgpt-terminal.git

## To Run
1. Ensure **Python 3.10+** is installed on your system.  
2. Create a `.env` file in the project folder and add your OpenAI API key like this:  
   ```
   OPENAI_API_KEY=your_key_here
   ```
3. Install dependencies (if required):  
   ```
   pip install openai python-dotenv
   ```
4. Run the program:  
   ```
   python main.py
   ```
5. Type messages directly into the terminal to chat, or type `exit` to quit.

