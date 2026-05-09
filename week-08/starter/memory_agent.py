"""
Week 8 Build: Memory-Aware DevOps Assistant

Implements all 4 memory types:
- In-context: conversation history
- External: team profiles (JSON file)
- Episodic: past incidents (JSON file + ChromaDB search)
- Semantic: runbook rules (ChromaDB)

Usage:
    python memory_agent.py
"""

import os
import json
from datetime import datetime
from pathlib import Path
import anthropic
import chromadb
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"

MEMORY_DIR = Path("memory")
TEAM_FILE = MEMORY_DIR / "team.json"
INCIDENTS_FILE = MEMORY_DIR / "incidents.json"

# Create memory directory if it doesn't exist
MEMORY_DIR.mkdir(exist_ok=True)


# ── External Memory: Team Profiles ────────────

def load_team_profiles() -> dict:
    """Load team member profiles from disk."""
    if TEAM_FILE.exists():
        return json.loads(TEAM_FILE.read_text())
    # Default team for first run
    return {
        "alice": {"role": "SRE Lead", "specialties": ["kubernetes", "networking"], "on_call": True},
        "bob": {"role": "Java Dev", "specialties": ["payment-api", "order-service"], "on_call": False},
        "carol": {"role": "DevOps", "specialties": ["CI/CD", "terraform", "AWS"], "on_call": False},
    }


def save_team_profiles(profiles: dict):
    """Save team profiles to disk."""
    TEAM_FILE.write_text(json.dumps(profiles, indent=2))


# ── Episodic Memory: Past Incidents ──────────

def load_incidents() -> list[dict]:
    """Load past incidents from disk."""
    if INCIDENTS_FILE.exists():
        return json.loads(INCIDENTS_FILE.read_text())
    return []


def save_incident(incident: dict):
    """Append a new incident to the incident log."""
    incidents = load_incidents()
    incident["timestamp"] = datetime.now().isoformat()
    incidents.append(incident)
    INCIDENTS_FILE.write_text(json.dumps(incidents, indent=2))
    print(f"[MEMORY] Saved incident to episodic memory: {incident.get('title', 'unknown')}")


def find_similar_incidents(query: str, top_k: int = 2) -> list[dict]:
    """
    TODO 1: Use ChromaDB to find past incidents similar to the query.
    - Load all incidents
    - Store in ChromaDB (or build the collection fresh each time)
    - Query by similarity to `query`
    - Return the top_k most similar incidents
    """
    incidents = load_incidents()
    if not incidents:
        return []
    # TODO: Implement ChromaDB similarity search over incident descriptions
    # For now, return the 2 most recent as a placeholder
    return incidents[-top_k:]


# ── Semantic Memory: Runbook Rules ────────────

RUNBOOK_RULES = [
    "P1 incidents require a war room to be opened within 10 minutes.",
    "All service restarts must be approved by the on-call SRE lead.",
    "Incident tickets must include: service name, start time, impact, and root cause.",
    "payment-api 503 errors above 10%: check HPA limits and database connection pool first.",
    "Rollbacks should be the last resort; prefer feature flags to disable broken code.",
]


def build_runbook_store() -> chromadb.Collection:
    """Build a ChromaDB collection of runbook rules."""
    # TODO 2: Create a ChromaDB client and collection named "runbook"
    # Add RUNBOOK_RULES as documents
    # Return the collection
    pass


def get_relevant_rules(query: str, collection: chromadb.Collection, top_k: int = 2) -> str:
    """Retrieve the most relevant runbook rules for a query."""
    # TODO 3: Query the collection and return the top_k rules as a formatted string
    pass


# ── The Memory-Aware Agent ────────────────────

def run_memory_agent():
    """Main agent loop with all 4 memory types active."""
    print("Memory-Aware DevOps Assistant")
    print("Commands: 'add team <name> <role>', 'save incident', 'quit'\n")

    # Load all memory types
    team = load_team_profiles()
    conversation: list[dict] = []   # In-context memory
    runbook_store = build_runbook_store()  # Semantic memory

    # Build system prompt with external memory (team info)
    team_summary = "\n".join([f"- {name}: {info['role']}, specialties: {', '.join(info['specialties'])}"
                               for name, info in team.items()])

    system_prompt = f"""You are a DevOps incident response assistant with memory of past incidents and team knowledge.

TEAM:
{team_summary}

INSTRUCTIONS:
- When an incident is described, check if you've seen something similar before
- Reference relevant team members by name based on their specialties
- Follow the runbook rules provided in context
- Be concise and action-oriented"""

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            break

        if user_input.lower().startswith("save incident"):
            # TODO 4: Extract incident details from conversation and save to episodic memory
            pass

        # TODO 5: Find similar past incidents (episodic memory)
        # similar = find_similar_incidents(user_input)

        # TODO 6: Get relevant runbook rules (semantic memory)
        # rules = get_relevant_rules(user_input, runbook_store)

        # TODO 7: Build context string combining episodic + semantic memory
        # Include in the user message as additional context

        # TODO 8: Add to conversation (in-context memory) and call Claude
        # Print the response
        pass


if __name__ == "__main__":
    run_memory_agent()
