"""
Week 6 Build: LangGraph Stateful DevOps Agent

Features:
- Multi-step tool-calling agent
- Persistent state across steps
- Human-in-the-loop approval for destructive actions

Usage:
    python langgraph_agent.py
"""

import os
from typing import TypedDict, Annotated, Sequence
from dotenv import load_dotenv
import anthropic

load_dotenv()

# ─────────────────────────────────────────────
# NOTE: After completing the DeepLearning.AI course,
# you'll know how to use LangGraph's StateGraph directly.
# This starter uses a simplified manual state machine
# so you understand the concepts before the framework.
# ─────────────────────────────────────────────

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"

# ── State Definition ──────────────────────────

class AgentState(TypedDict):
    incident: str
    messages: list[dict]
    tool_results: list[dict]
    next_action: str          # "search_runbook" | "check_metrics" | "create_ticket" | "needs_approval" | "done"
    awaiting_approval: bool
    final_summary: str


# ── Simulated Tools ───────────────────────────

def search_runbook(query: str) -> str:
    """Simulate searching an internal runbook."""
    # TODO 1: Return a mock runbook entry for the query
    # In production this would query ChromaDB or Confluence
    return f"[RUNBOOK] For '{query}': Check pod logs with kubectl logs -n prod, then verify HPA settings."


def check_metrics(service: str) -> str:
    """Simulate fetching service metrics."""
    # TODO 2: Return mock metrics for the service
    return f"[METRICS] {service}: CPU 87%, Memory 92%, Error rate 40%, P99 latency 8.2s"


def create_ticket(summary: str) -> str:
    """Simulate creating a JIRA/GitHub issue."""
    # TODO 3: Return a mock ticket ID
    return f"[TICKET] Created INC-{hash(summary) % 10000}: {summary[:50]}"


def restart_service(service: str) -> str:
    """DESTRUCTIVE: Restart a Kubernetes deployment. Requires human approval."""
    return f"[ACTION] kubectl rollout restart deployment/{service} -n prod — EXECUTED"


# ── Agent Nodes ───────────────────────────────

def decide_action(state: AgentState) -> AgentState:
    """
    LLM decides what to do next based on current state.
    This is the 'brain' of the agent.
    """
    # TODO 4: Build a prompt that includes:
    # - The original incident
    # - Any tool results so far
    # - Available actions: search_runbook, check_metrics, create_ticket, restart_service, done
    # Ask Claude to decide the next action and return it as JSON:
    # {"action": "search_runbook", "parameter": "payment-api 503 errors"}

    # Parse the JSON response and update state["next_action"]
    pass


def execute_tool(state: AgentState) -> AgentState:
    """Execute the tool chosen by decide_action."""
    # TODO 5: Based on state["next_action"], call the appropriate tool function
    # For "restart_service": set state["awaiting_approval"] = True instead of executing
    # Store the tool result in state["tool_results"]
    pass


def request_human_approval(state: AgentState) -> str:
    """Ask the human for approval before a destructive action."""
    # TODO 6: Print a clear approval request to the terminal
    # Return "approved" or "rejected" based on user input
    pass


def summarize(state: AgentState) -> AgentState:
    """Generate final incident summary."""
    # TODO 7: Call Claude to summarize all tool results and actions taken
    # Store in state["final_summary"]
    pass


# ── Agent Loop ────────────────────────────────

def run_agent(incident: str, max_steps: int = 5):
    """Run the agent loop until done or max_steps reached."""
    state: AgentState = {
        "incident": incident,
        "messages": [],
        "tool_results": [],
        "next_action": "start",
        "awaiting_approval": False,
        "final_summary": "",
    }

    print(f"\nIncident: {incident}")
    print("=" * 50)

    for step in range(max_steps):
        print(f"\n[Step {step + 1}]")

        # TODO 8: Implement the agent loop:
        # 1. Call decide_action(state) to get next action
        # 2. If next_action == "done": break
        # 3. If awaiting_approval: call request_human_approval(); if rejected, set next_action = "done"
        # 4. Otherwise: call execute_tool(state)
        # 5. Print current tool results for visibility
        pass

    summarize(state)
    print(f"\n{'='*50}\nFINAL SUMMARY:\n{state['final_summary']}")


if __name__ == "__main__":
    run_agent(
        "payment-api is returning 503 errors, 40% failure rate since 14:32 UTC. "
        "Checkout and order confirmation affected."
    )
