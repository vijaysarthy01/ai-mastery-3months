"""
Week 4 Build: RAG Q&A Bot

Loads documents from a docs/ folder, stores them in ChromaDB,
and answers questions using Claude with retrieved context.

Usage:
    python rag_bot.py
"""

import os
import glob
import anthropic
import chromadb
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"
DOCS_FOLDER = "docs"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 3  # Number of chunks to retrieve


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping chunks."""
    # TODO 1: Split `text` into chunks of `chunk_size` characters
    # Each chunk should overlap with the previous by `overlap` characters
    # Return a list of chunk strings
    # Hint: use a while loop with a sliding window
    pass


def load_documents(folder: str) -> list[dict]:
    """Load all .txt files from the docs folder."""
    # TODO 2: Use glob to find all .txt files in `folder`
    # For each file, read its contents and chunk it
    # Return a list of dicts: {"text": chunk, "source": filename, "chunk_id": "filename_0"}
    pass


def build_vector_store(documents: list[dict]) -> chromadb.Collection:
    """Create a ChromaDB collection and add documents."""
    # TODO 3: Create a ChromaDB in-memory client: chromadb.Client()
    # Create or get a collection named "documents"
    # Add all document chunks with:
    #   - documents: list of text strings
    #   - ids: list of chunk_id strings
    #   - metadatas: list of {"source": filename} dicts
    # Return the collection
    pass


def retrieve_context(collection: chromadb.Collection, query: str, top_k: int = TOP_K) -> str:
    """Find the most relevant chunks for a query."""
    # TODO 4: Query the collection with collection.query(query_texts=[query], n_results=top_k)
    # Format the results as a single string with source labels
    # Example: "From runbook.txt:\n<chunk text>\n\nFrom incident_log.txt:\n<chunk text>"
    pass


def answer_question(context: str, question: str) -> str:
    """Use Claude to answer a question given retrieved context."""
    # TODO 5: Build a prompt that includes the context and question
    # Tell Claude to answer only based on the provided context
    # If the answer is not in the context, Claude should say so
    # Call the Claude API and return the response text
    pass


def main():
    print("Loading documents...")
    documents = load_documents(DOCS_FOLDER)

    if not documents:
        print(f"No .txt files found in '{DOCS_FOLDER}/' folder.")
        print("Create a docs/ folder with some .txt files and try again.")
        return

    print(f"Loaded {len(documents)} chunks from {DOCS_FOLDER}/")

    print("Building vector store...")
    collection = build_vector_store(documents)
    print("Vector store ready.\n")

    print("Ask questions about your documents (type 'quit' to exit)\n")
    print("-" * 50)

    while True:
        question = input("\nQuestion: ").strip()
        if question.lower() == "quit":
            break
        if not question:
            continue

        context = retrieve_context(collection, question)
        answer = answer_question(context, question)
        print(f"\nAnswer: {answer}")


if __name__ == "__main__":
    main()
