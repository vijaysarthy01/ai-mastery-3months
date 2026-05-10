"""
Day 5 Build: Interactive AI Tutor CLI

A streaming chatbot powered by Claude that teaches Python and AI concepts.
Demonstrates: Claude API, streaming, multi-turn conversation, file I/O.

Usage:
    python tutor.py

Requirements:
    pip install anthropic python-dotenv
    ANTHROPIC_API_KEY in .env file
"""

import anthropic
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are an expert Python and AI tutor teaching a beginner.

Your teaching style:
- Use simple analogies from everyday life
- Always give a brief code example
- After explaining, ask one follow-up question to check understanding
- Use the Socratic method — guide to discovery rather than just telling
- Keep responses concise (3-5 short paragraphs max)
- When the user answers correctly, celebrate it!

Current curriculum: Python fundamentals → AI APIs → Agent development
"""

SESSION_FILE = "tutor_session.json"


def save_session(history: list) -> None:
    with open(SESSION_FILE, "w") as f:
        json.dump({"saved_at": datetime.now().isoformat(), "messages": history}, f, indent=2)
    print(f"Session saved.")


def load_session() -> list:
    if os.path.exists(SESSION_FILE):
        try:
            with open(SESSION_FILE, "r") as f:
                data = json.load(f)
            print(f"Loaded previous session ({len(data['messages'])} messages).")
            return data["messages"]
        except (json.JSONDecodeError, KeyError):
            print("Could not load previous session. Starting fresh.")
    return []


def tutor_chat(history: list, user_input: str) -> list:
    history.append({"role": "user", "content": user_input})

    print("\nTutor: ", end="", flush=True)
    full_response = ""

    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=history
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_response += text

    print("\n")
    history.append({"role": "assistant", "content": full_response})
    return history


def main():
    print("=" * 50)
    print("  AI-Powered Python Tutor")
    print("  Commands: 'save', 'clear', 'quit'")
    print("=" * 50)

    history = load_session()

    if not history:
        print("\nWhat Python concept would you like to explore today?\n")
    else:
        print("\nContinuing your previous session. What would you like to work on?\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        elif user_input.lower() == "quit":
            save_session(history)
            print("Great work! Keep practicing. See you tomorrow!")
            break
        elif user_input.lower() == "save":
            save_session(history)
            continue
        elif user_input.lower() == "clear":
            history = []
            print("Session cleared. Fresh start!\n")
            continue

        history = tutor_chat(history, user_input)


if __name__ == "__main__":
    main()
