"""
Week 5 Build: Anthropic Agent Patterns

Implements the 4 core patterns from:
https://www.anthropic.com/research/building-effective-agents

Test case: DevOps incident report generation
"""

import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"

INCIDENT_INPUT = """
Service: payment-api
Alert: 503 errors spike — 40% of requests failing
Time: 14:32 UTC
Affected: checkout flow, order confirmation
On-call: Team Alpha
"""


def call_claude(system: str, user: str) -> str:
    """Helper: single Claude call, returns text."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    return response.content[0].text


# ─────────────────────────────────────────────
# PATTERN 1: PROMPT CHAINING
# ─────────────────────────────────────────────

def pattern_chaining(incident: str) -> str:
    """
    3-step chain: Diagnose → Draft Timeline → Write Incident Report

    TODO 1: Implement each step as a separate call_claude() call
    Step 1: Given the incident data, diagnose the likely root cause
    Step 2: Given the diagnosis, draft a timeline of events
    Step 3: Given the diagnosis + timeline, write a formal incident report
    Return the final incident report.
    """
    print("\n[PATTERN 1: PROMPT CHAINING]")
    # Step 1: Diagnose
    # TODO: call_claude() to diagnose root cause from `incident`

    # Step 2: Draft timeline
    # TODO: call_claude() to draft timeline from diagnosis

    # Step 3: Write report
    # TODO: call_claude() to write formal report from diagnosis + timeline
    pass


# ─────────────────────────────────────────────
# PATTERN 2: ROUTING
# ─────────────────────────────────────────────

def pattern_routing(incident: str) -> str:
    """
    Classify severity, then route to appropriate handler.

    TODO 2: Step 1 — classify severity as "P1", "P2", or "P3"
    Step 2 — based on classification:
      P1 → escalation_handler() (war room, exec notification)
      P2 → standard_handler() (on-call team response)
      P3 → log_handler() (ticket created, no immediate action)
    """
    print("\n[PATTERN 2: ROUTING]")

    def escalation_handler(incident: str) -> str:
        # TODO: call_claude() to generate a P1 war room escalation message
        pass

    def standard_handler(incident: str) -> str:
        # TODO: call_claude() to generate a standard P2 incident response plan
        pass

    def log_handler(incident: str) -> str:
        # TODO: call_claude() to generate a P3 log entry / ticket description
        pass

    # TODO: Classify, then call the right handler
    pass


# ─────────────────────────────────────────────
# PATTERN 3: ORCHESTRATOR-WORKERS
# ─────────────────────────────────────────────

def pattern_orchestrator_workers(incident: str) -> str:
    """
    Orchestrator plans subtasks, workers execute in parallel.

    TODO 3:
    Step 1 (Orchestrator): Ask Claude to break the incident response into 3 parallel tasks
    Step 2 (Workers): Execute each task as a separate call_claude() call
    Step 3: Aggregate all worker outputs into a final summary
    """
    print("\n[PATTERN 3: ORCHESTRATOR-WORKERS]")
    # Hint: define 3 fixed worker roles — infrastructure, application, communications
    pass


# ─────────────────────────────────────────────
# PATTERN 4: EVALUATOR-OPTIMIZER
# ─────────────────────────────────────────────

def pattern_evaluator_optimizer(incident: str, max_iterations: int = 3) -> str:
    """
    Generate incident report → evaluate quality → refine until score >= 8.

    TODO 4:
    Step 1 (Generator): Generate an incident report
    Step 2 (Evaluator): Score it 1-10 and explain what's missing
    Step 3: If score < 8, call Generator again with the feedback
    Repeat up to max_iterations times.
    Return the best version.
    """
    print("\n[PATTERN 4: EVALUATOR-OPTIMIZER]")
    pass


if __name__ == "__main__":
    print("=" * 60)
    print("ANTHROPIC AGENT PATTERNS DEMO")
    print("=" * 60)

    result1 = pattern_chaining(INCIDENT_INPUT)
    print(result1)

    result2 = pattern_routing(INCIDENT_INPUT)
    print(result2)

    result3 = pattern_orchestrator_workers(INCIDENT_INPUT)
    print(result3)

    result4 = pattern_evaluator_optimizer(INCIDENT_INPUT)
    print(result4)
