"""
Week 3 Build: Multi-turn Streaming Chat App

Features:
- Persistent conversation history
- Real-time streaming output
- Token usage tracking
- Configurable system prompt

Usage:
    python chat_app.py
"""

import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"

# TODO 1: Define a SYSTEM_PROMPT for a DevOps expert assistant
SYSTEM_PROMPT = ""


def chat(conversation_history: list, user_message: str) -> tuple[str, dict]:
    """
    Send a message and stream the response.

    Returns:
        tuple: (full_response_text, usage_stats)
    """
    # TODO 2: Append the user message to conversation_history
    # Format: {"role": "user", "content": user_message}

    # TODO 3: Use client.messages.stream() as a context manager to stream the response
    # Pass: model, max_tokens=2048, system=SYSTEM_PROMPT, messages=conversation_history
    # Inside the context manager, iterate over the stream and print each text chunk
    # Hint: use `with client.messages.stream(...) as stream:`
    #       then `for text in stream.text_stream: print(text, end="", flush=True)`

    # TODO 4: After streaming, get the final message with stream.get_final_message()
    # Extract: full text (from message.content[0].text) and usage (message.usage)

    # TODO 5: Append Claude's response to conversation_history
    # Format: {"role": "assistant", "content": full_response_text}

    # TODO 6: Return (full_response_text, usage)
    pass


def main():
    conversation_history = []
    print("DevOps AI Assistant (type 'quit' to exit)\n")
    print(f"System: {SYSTEM_PROMPT}\n")
    print("-" * 50)

    while True:
        # TODO 7: Get input from the user
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if not user_input:
            continue

        print("\nAssistant: ", end="")

        # TODO 8: Call chat() and handle the response
        # After the streamed response, print a newline and token usage stats
        # Format: "\n[Tokens used - Input: X, Output: Y]"


if __name__ == "__main__":
    main()
