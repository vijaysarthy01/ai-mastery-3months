# Week 11: Agent2Agent (A2A) Protocol

## Goal
Learn how agents built on different frameworks communicate with each other. This is the cutting edge of agentic AI in 2025-2026.

---

## Watch + Build (free)

| Resource | URL |
|----------|-----|
| A2A: The Agent2Agent Protocol | https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/ |
| A2A GitHub | https://github.com/google-a2a/A2A |
| A2A Spec | https://google-a2a.github.io/A2A/ |

Note: This course is co-authored by **IBM Research** — highly relevant given your IBM Integration Bus background. The protocol concepts map directly to service-oriented architecture you already know.

---

## Key A2A Concepts

```
Agent Card     — A JSON file describing what an agent can do (like a service contract)
Task           — A unit of work sent from one agent to another
TaskState      — submitted → working → completed/failed
Push vs Pull   — Agents can push updates or clients can poll for status
Multi-turn     — Agent-to-agent conversations with state
```

---

## The SOA Connection (Your Background)

| SOA Concept | A2A Equivalent |
|-------------|---------------|
| WSDL / Service Contract | Agent Card (agent.json) |
| Service Endpoint | Agent URL |
| Message Exchange Pattern | Task lifecycle |
| ESB routing | Orchestrating agent |

---

## Build Assignment

**Build two agents that communicate via A2A protocol.**

Agent 1 (Orchestrator): Receives incident reports, decides which specialist agent to call
Agent 2 (Specialist): A database expert agent that answers database-related queries

Connect them so that:
1. Orchestrator receives: "payment-api has database connection timeouts"
2. Orchestrator detects: database issue → routes to DB Specialist
3. DB Specialist responds with diagnosis + recommendations
4. Orchestrator returns consolidated response

**Starter file:** `starter/a2a_agent.py`

---

## Quiz

1. How is the A2A Agent Card similar to a WSDL in SOA? What does each describe?
2. What problem does A2A solve that calling a Python function directly does not?
3. How would you use A2A to connect a LangGraph agent to a CrewAI agent?
