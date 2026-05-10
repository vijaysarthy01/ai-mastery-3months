"""
Week 1 Build: CLI Text Summarizer using Claude API

Usage:
    python summarizer.py <path_to_text_file>

Example:
    python summarizer.py my_notes.txt
"""

import sys
import os

# TODO 1: Import the anthropic library
import anthropic
from dotenv import load_dotenv


# TODO 2: Import load_dotenv from dotenv and call load_dotenv()
# This loads your ANTHROPIC_API_KEY from the .env file# from dotenv import load_dotenv
load_dotenv()




def read_file(filepath: str) -> str:
    """Read and return the contents of a text file."""
    # TODO 3: Open the file at `filepath`, read its contents, and return them.
    # Handle the case where the file doesn't exist with a helpful error message.
    if not os.path.isfile(filepath):
            print(f"Error: File '{filepath}' does not exist.")
            sys.exit(1)
    with open(filepath, "r") as file:
            return file.read()


def summarize_text(text: str) -> str:
    """Send text to Claude and return a summary."""
    # TODO 4: Create an Anthropic client instance
    client = anthropic.Anthropic()

    # TODO 5: Call client.messages.create() with:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "assistant", "content": f"Please summarize the following text:\n\n{text}"}]
    )

    # TODO 6: Extract the text from the response and return it
    # Hint: response.content[0].text
    return response.content[0].text


def main():
    # TODO 7: Check that the user provided a filename argument (sys.argv)
    # If not, print usage instructions and exit
    if len(sys.argv) < 2:
        print("Usage: python summarizer.py <path_to_text_file>")
        sys.exit(1)

    # TODO 8: Get the filename from sys.argv[1]
    filename = sys.argv[1]

    # TODO 9: Call read_file() to get the file contents
    file_contents = read_file(filename)

    # TODO 10: Call summarize_text() with the contents
    summary = summarize_text(file_contents)
    # TODO 11: Print the summary
    print(summary)


if __name__ == "__main__":
    main()
