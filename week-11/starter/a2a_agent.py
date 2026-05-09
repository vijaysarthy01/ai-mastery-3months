"""
Week 11 Build: Agent2Agent (A2A) Communication

Two agents that communicate via HTTP using the A2A protocol concepts:
- OrchestratorAgent: routes incidents to specialist agents
- DBSpecialistAgent: answers database-related queries

This simplified implementation demonstrates A2A concepts without
requiring the full A2A SDK setup. After completing the DeepLearning.AI
course, upgrade this to use the official A2A Python library.

Usage:
    # Terminal 1: Start the DB Specialist agent server
    python a2a_agent.py --role specialist --port 8001

    # Terminal 2: Start the Orchestrator agent (calls the specialist)
    python a2a_agent.py --role orchestrator --port 8000
"""

import os
import json
import argparse
import anthropic
import httpx
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"


# ── A2A Data Models ───────────────────────────

class AgentCard(BaseModel):
    """Describes what this agent can do (the A2A 'service contract')."""
    name: str
    description: str
    capabilities: list[str]
    endpoint: str


class Task(BaseModel):
    """A unit of work sent from one agent to another."""
    task_id: str
    description: str
    context: dict = {}


class TaskResult(BaseModel):
    """The response from an agent after completing a task."""
    task_id: str
    status: str   # "completed" | "failed"
    result: str
    agent_name: str


# ── DB Specialist Agent ───────────────────────

def create_specialist_app() -> FastAPI:
    app = FastAPI(title="DB Specialist Agent")

    # TODO 1: Define the Agent Card for the DB Specialist
    AGENT_CARD = AgentCard(
        name="DB Specialist",
        description="Expert in PostgreSQL, connection pooling, and database performance",
        capabilities=[
            "diagnose database connection issues",
            "analyze slow query problems",
            "recommend connection pool settings",
            "identify lock contention"
        ],
        endpoint="http://localhost:8001"
    )

    @app.get("/.well-known/agent.json")
    def get_agent_card():
        """Return the Agent Card (A2A discovery endpoint)."""
        return AGENT_CARD

    @app.post("/tasks")
    def handle_task(task: Task) -> TaskResult:
        """
        TODO 2: Process the incoming task using Claude.
        - Build a system prompt for a database expert
        - Call Claude with the task description
        - Return a TaskResult with the diagnosis
        """
        pass

    return app


# ── Orchestrator Agent ────────────────────────

def create_orchestrator_app() -> FastAPI:
    app = FastAPI(title="Orchestrator Agent")

    SPECIALIST_URL = "http://localhost:8001"

    def discover_specialist(url: str) -> AgentCard:
        """TODO 3: Fetch and parse the specialist's Agent Card from {url}/.well-known/agent.json"""
        pass

    def route_to_specialist(incident: str, specialist_url: str) -> str:
        """
        TODO 4: Send a task to the specialist agent and return its response.
        POST to {specialist_url}/tasks with a Task payload.
        Parse and return the TaskResult.result.
        """
        pass

    def should_route_to_db_specialist(incident: str) -> bool:
        """
        TODO 5: Use Claude to classify whether the incident is database-related.
        Return True if it involves: database, connection, timeout, pool, query, postgres
        """
        pass

    @app.post("/incidents")
    def handle_incident(payload: dict) -> dict:
        """
        TODO 6: Main orchestration logic.
        1. Receive incident description
        2. Classify: is it database-related?
        3. If yes: route to DB Specialist and return specialist's answer
        4. If no: handle directly with Claude (general DevOps answer)
        """
        pass

    return app


# ── Main ──────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--role", choices=["specialist", "orchestrator"], required=True)
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    if args.role == "specialist":
        app = create_specialist_app()
        print(f"DB Specialist Agent running on port {args.port}")
        print(f"Agent Card: http://localhost:{args.port}/.well-known/agent.json")
    else:
        app = create_orchestrator_app()
        print(f"Orchestrator Agent running on port {args.port}")
        print(f"Send incidents to: POST http://localhost:{args.port}/incidents")
        print(f'Example: curl -X POST http://localhost:{args.port}/incidents \\')
        print('  -H "Content-Type: application/json" \\')
        print('  -d \'{"description": "payment-api has database connection timeouts"}\'')

    uvicorn.run(app, host="0.0.0.0", port=args.port)
