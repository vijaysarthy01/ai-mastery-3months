"""
Week 2 Build: Dynamic Prompt Template System

Demonstrates: zero-shot, few-shot, chain-of-thought, structured output (JSON)

Usage:
    python prompt_templates.py
"""

import json
import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"


# TODO 1: Define a SYSTEM_PROMPTS dictionary with keys "summarize", "classify", "extract"
# Each value should be a system prompt string that tells Claude its role for that task.
SYSTEM_PROMPTS = {
    "summarize": "",   # TODO: Write a system prompt for a summarization assistant
    "classify":  "",   # TODO: Write a system prompt for a text classifier (categories: positive/negative/neutral)
    "extract":   "",   # TODO: Write a system prompt for an information extractor that returns JSON
}


def build_few_shot_prompt(task: str, user_text: str) -> str:
    """Build a prompt with examples for the given task."""
    # TODO 2: For the "classify" task, add 2-3 examples before the actual user_text
    # Example format:
    #   Text: "The product was fantastic!"
    #   Classification: {"label": "positive", "confidence": "high"}
    #
    #   Text: "It was okay, nothing special."
    #   Classification: {"label": "neutral", "confidence": "medium"}
    #
    #   Text: <user_text>
    #   Classification:
    #
    # For other tasks, return a simple prompt without examples.
    pass


def call_claude(system_prompt: str, user_prompt: str) -> str:
    """Call Claude with a system prompt and user message."""
    # TODO 3: Use client.messages.create() with the system and user prompts
    # Return the text content of the response
    pass


def parse_json_response(response: str) -> dict:
    """Safely parse a JSON response from Claude."""
    # TODO 4: Try to parse the response as JSON.
    # If it fails, return {"error": "Could not parse JSON", "raw": response}
    pass


def run_task(task: str, text: str):
    """Run a task and print the result."""
    print(f"\n--- Task: {task.upper()} ---")
    print(f"Input: {text[:80]}...")

    # TODO 5: Get the system prompt for this task
    # Call build_few_shot_prompt() to get the user prompt
    # Call call_claude() with both
    # For "extract" and "classify" tasks, also call parse_json_response()
    # Print the result
    pass


if __name__ == "__main__":
    # Test all three task types
    sample_text = """
    The quarterly earnings report shows a 23% increase in revenue compared to last year.
    The DevOps team reduced deployment time by 40% through pipeline automation.
    However, customer satisfaction scores dropped slightly from 4.2 to 3.9 out of 5.
    The engineering team plans to address this with a new on-call rotation starting next month.
    """

    run_task("summarize", sample_text)
    run_task("classify", sample_text)
    run_task("extract", sample_text)
