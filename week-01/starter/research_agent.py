"""
Day 6 Build: Research Agent with Wikipedia Tool

An AI agent that uses tool calling to search Wikipedia and answer questions.
Demonstrates: tool use, the agentic loop, multi-turn with tool results.

Usage:
    python research_agent.py

Requirements:
    pip install anthropic requests python-dotenv
    ANTHROPIC_API_KEY in .env file
"""

import anthropic
import os
import requests
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# --- Tool Implementations ---

def search_wikipedia(query: str, sentences: int = 5) -> str:
    """Search Wikipedia and return a plain-text summary."""
    try:
        url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query.replace(" ", "_")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            extract = response.json().get("extract", "No information found.")
            parts = extract.split(". ")
            return ". ".join(parts[:sentences]) + "."
        elif response.status_code == 404:
            return f"No Wikipedia article found for '{query}'."
        else:
            return f"Search failed with status {response.status_code}."
    except Exception as e:
        return f"Search error: {e}"


def get_current_date() -> str:
    from datetime import datetime
    return datetime.now().strftime("%B %d, %Y")


# --- Tool Schemas ---

TOOLS = [
    {
        "name": "search_wikipedia",
        "description": (
            "Search Wikipedia for information about a topic. "
            "Good for facts, definitions, historical information, and overviews."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "The topic to search for"},
                "sentences": {
                    "type": "integer",
                    "description": "Number of sentences to return (1-10)",
                    "default": 5
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "get_current_date",
        "description": "Get the current date. Use for time-sensitive topics.",
        "input_schema": {"type": "object", "properties": {}}
    }
]

TOOL_MAP = {
    "search_wikipedia": search_wikipedia,
    "get_current_date": get_current_date
}

SYSTEM_PROMPT = """You are a research assistant. When answering questions:
1. Search for relevant information using available tools
2. Synthesize findings into a clear, accurate response
3. Cite your sources
4. Perform multiple searches if needed
5. Be honest about what you don't know"""


# --- Agentic Loop ---

def research_agent(question: str) -> None:
    messages = [{"role": "user", "content": question}]
    print(f"\nResearching: {question}\n")

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2048,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages
        )

        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    print(f"Answer:\n{block.text}")
            return

        elif response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    print(f"  Searching: {block.input.get('query', block.name)}...")
                    func = TOOL_MAP.get(block.name)
                    result = func(**block.input) if func else "Tool not found"
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            messages.append({"role": "user", "content": tool_results})

        else:
            print(f"Unexpected stop reason: {response.stop_reason}")
            return


def main():
    print("=== Research Agent ===")
    print("Ask me anything. I'll search Wikipedia to answer.\n")

    while True:
        question = input("You: ").strip()
        if not question:
            continue
        if question.lower() in ("quit", "exit"):
            break
        research_agent(question)
        print()


if __name__ == "__main__":
    main()
