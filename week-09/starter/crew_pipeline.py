"""
Week 9 Build: 3-Agent CrewAI DevOps Pipeline

Agents:
1. Monitor Agent   — Analyzes logs and extracts anomalies
2. Diagnosis Agent — Identifies root cause from Monitor's findings
3. Reporter Agent  — Writes a formal incident report

Usage:
    python crew_pipeline.py
"""

import os
from dotenv import load_dotenv

load_dotenv()

# TODO 1: Import crewai components
# from crewai import Agent, Task, Crew, Process
# from crewai_tools import tool  (or define custom tools below)


# ── Simulated Log Data ────────────────────────

SAMPLE_LOGS = """
2026-05-09 14:30:01 INFO  payment-api pod/payment-api-7d8f9-abc Starting request processing
2026-05-09 14:30:45 ERROR payment-api pod/payment-api-7d8f9-abc Database connection timeout after 30s
2026-05-09 14:30:46 ERROR payment-api pod/payment-api-7d8f9-abc Database connection timeout after 30s
2026-05-09 14:30:47 WARN  payment-api pod/payment-api-7d8f9-def Connection pool exhausted (max: 20)
2026-05-09 14:30:48 ERROR payment-api pod/payment-api-7d8f9-abc HTTP 503 returned to client
2026-05-09 14:31:02 ERROR payment-api pod/payment-api-7d8f9-def HTTP 503 returned to client
2026-05-09 14:31:15 ERROR payment-api pod/payment-api-7d8f9-ghi HTTP 503 returned to client
2026-05-09 14:32:00 INFO  postgres   pod/postgres-primary-1     CPU at 94%, slow query log enabled
2026-05-09 14:32:01 WARN  postgres   pod/postgres-primary-1     Query exceeded 5000ms: SELECT * FROM orders
2026-05-09 14:32:30 ERROR postgres   pod/postgres-primary-1     Max connections reached (100/100)
"""


# ── Custom Tools ──────────────────────────────

# TODO 2: Define a @tool for searching runbook
# def search_runbook(query: str) -> str:
#     """Search the internal runbook for resolution steps."""
#     ...

# TODO 3: Define a @tool for checking recent deployments
# def check_deployments(service: str) -> str:
#     """Check recent deployment history for a service."""
#     ...


# ── Agent Definitions ─────────────────────────

# TODO 4: Define the Monitor Agent
# monitor_agent = Agent(
#     role="Infrastructure Monitor",
#     goal="Analyze log data to identify anomalies, errors, and warning patterns",
#     backstory="You are a seasoned SRE who has seen thousands of incidents. "
#               "You quickly spot the signal in noisy logs.",
#     tools=[],          # No tools needed — analyzes the log text directly
#     verbose=True,
#     llm="claude-sonnet-4-6"   # Note: CrewAI uses LLM strings or LLM objects
# )

# TODO 5: Define the Diagnosis Agent
# diagnosis_agent = Agent(...)

# TODO 6: Define the Reporter Agent
# reporter_agent = Agent(...)


# ── Task Definitions ──────────────────────────

# TODO 7: Define Task 1 — Log Analysis
# monitor_task = Task(
#     description=f"Analyze the following logs and identify: "
#                 f"1) All error events 2) Patterns and frequency 3) Affected services\n\nLOGS:\n{SAMPLE_LOGS}",
#     expected_output="A structured analysis with: error list, patterns, affected services, and timeline",
#     agent=monitor_agent
# )

# TODO 8: Define Task 2 — Root Cause Diagnosis (uses output from Task 1)
# diagnosis_task = Task(...)

# TODO 9: Define Task 3 — Incident Report (uses output from Tasks 1 and 2)
# report_task = Task(
#     description="Write a formal incident report based on the log analysis and diagnosis.",
#     expected_output="""A formal incident report with sections:
#     - Incident Title
#     - Severity (P1/P2/P3)
#     - Timeline
#     - Root Cause
#     - Impact
#     - Immediate Actions Taken
#     - Follow-up Actions Required""",
#     agent=reporter_agent
# )


# ── Crew Assembly ─────────────────────────────

# TODO 10: Create and run the Crew
# crew = Crew(
#     agents=[monitor_agent, diagnosis_agent, reporter_agent],
#     tasks=[monitor_task, diagnosis_task, report_task],
#     process=Process.sequential,
#     verbose=True
# )

if __name__ == "__main__":
    print("Starting DevOps Incident Response Crew...")
    print("=" * 60)

    # TODO 11: Run the crew and print the result
    # result = crew.kickoff()
    # print("\n" + "=" * 60)
    # print("FINAL INCIDENT REPORT:")
    # print(result)

    print("Uncomment the crew code above after completing the DeepLearning.AI CrewAI course.")
    print("Course: https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/")
