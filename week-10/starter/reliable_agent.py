"""
Week 10 Build: Reliable Agent with Observability + Semantic Caching

Production features:
- Structured tracing to JSON
- Retry with exponential backoff
- Semantic caching with ChromaDB
- Output validation
- Cost tracking

Usage:
    python reliable_agent.py
"""

import os
import json
import time
import hashlib
from datetime import datetime
from pathlib import Path
import anthropic
import chromadb
from dotenv import load_dotenv

load_dotenv()

raw_client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"

TRACES_FILE = Path("traces.json")

# Approximate cost per 1M tokens (update from https://www.anthropic.com/pricing)
COST_PER_1M_INPUT_TOKENS = 3.00   # USD for claude-sonnet-4-6
COST_PER_1M_OUTPUT_TOKENS = 15.00


# ── Tracing ───────────────────────────────────

class Tracer:
    """Records LLM calls to a JSON trace file."""

    def __init__(self, filepath: Path = TRACES_FILE):
        self.filepath = filepath
        self.traces = []
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    def record(self, prompt: str, response: str, duration_ms: float, usage: dict):
        """TODO 1: Append a trace entry to self.traces and write to self.filepath"""
        # Entry should include: timestamp, prompt_preview (first 100 chars),
        # response_preview (first 100 chars), duration_ms, input_tokens, output_tokens
        # Also update self.total_input_tokens and self.total_output_tokens
        pass

    def print_cost_summary(self):
        """TODO 2: Print total tokens used and estimated USD cost."""
        pass


# ── Semantic Cache ────────────────────────────

class SemanticCache:
    """Cache LLM responses by semantic similarity using ChromaDB."""

    def __init__(self, similarity_threshold: float = 0.95):
        self.threshold = similarity_threshold
        # TODO 3: Initialize a ChromaDB in-memory client and "cache" collection
        pass

    def get(self, prompt: str) -> str | None:
        """Return cached response if a semantically similar prompt exists."""
        # TODO 4: Query the collection with the prompt
        # If distance < (1 - self.threshold), return the cached response
        # Otherwise return None
        pass

    def set(self, prompt: str, response: str):
        """Store a prompt-response pair in the cache."""
        # TODO 5: Add to the ChromaDB collection
        # Use a hash of the prompt as the document ID
        pass


# ── Retry Logic ───────────────────────────────

def call_with_retry(
    system: str,
    user: str,
    max_retries: int = 3,
    tracer: Tracer = None,
    cache: SemanticCache = None
) -> str:
    """Call Claude with retry, caching, and tracing."""

    # TODO 6: Check cache first — if hit, return cached response immediately

    # TODO 7: Retry loop with exponential backoff
    # for attempt in range(max_retries):
    #     try:
    #         start = time.time()
    #         response = raw_client.messages.create(...)
    #         duration_ms = (time.time() - start) * 1000
    #         text = response.content[0].text
    #         if tracer: tracer.record(user, text, duration_ms, response.usage.__dict__)
    #         if cache: cache.set(user, text)
    #         return text
    #     except anthropic.RateLimitError:
    #         sleep_time = 2 ** attempt  # 1s, 2s, 4s
    #         print(f"Rate limited. Retrying in {sleep_time}s...")
    #         time.sleep(sleep_time)
    #     except anthropic.APIStatusError as e:
    #         if e.status_code >= 500:  # Server error — retry
    #             time.sleep(2 ** attempt)
    #         else:
    #             raise  # Client error — don't retry
    pass


# ── Output Validation ─────────────────────────

def validate_incident_json(raw: str) -> dict:
    """
    TODO 8: Parse `raw` as JSON and validate it has required fields:
    - title (str)
    - severity (one of: P1, P2, P3)
    - root_cause (str)
    - actions (list)

    If valid, return the dict.
    If invalid, raise ValueError with a descriptive message.
    """
    pass


# ── Demo ──────────────────────────────────────

if __name__ == "__main__":
    tracer = Tracer()
    cache = SemanticCache(similarity_threshold=0.95)

    questions = [
        "payment-api is returning 503 errors. What should I check first?",
        "payment-api service is down with 503. What are the first steps?",  # Should hit cache
        "order-service has high latency. How do I diagnose it?",
    ]

    for i, question in enumerate(questions, 1):
        print(f"\n[Query {i}] {question}")
        response = call_with_retry(
            system="You are a DevOps expert. Be concise.",
            user=question,
            tracer=tracer,
            cache=cache
        )
        print(f"Response: {response[:200]}...")

    tracer.print_cost_summary()
