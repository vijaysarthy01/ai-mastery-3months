# Week 6: LangGraph — Stateful Agents

## Goal
Build a production-grade stateful agent using LangGraph. Learn the framework used by Klarna, Uber, and J.P. Morgan.

---

## Watch + Build (free, 1.5 hrs)

| Resource | URL |
|----------|-----|
| AI Agents in LangGraph (DeepLearning.AI) | https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/ |
| LangGraph Docs | https://docs.langchain.com/oss/python/langgraph/overview |

Complete the full DeepLearning.AI course (9 videos, 6 code examples). It's taught by Harrison Chase, the founder of LangChain.

---

## Key LangGraph Concepts

```
State       — A TypedDict that flows through the graph (shared memory between nodes)
Node        — A Python function that reads and writes to State
Edge        — Connects nodes (conditional edges = routing logic)
Graph       — The assembled pipeline of nodes + edges
Checkpoint  — Saves state to disk so agent survives interruptions (human-in-the-loop)
```

---

## Build Assignment

**Build a stateful DevOps troubleshooting agent with human-in-the-loop approval.**

The agent should:
1. Accept an incident description
2. Use tools: search_runbook, check_metrics, create_ticket
3. Decide next action based on tool results (multi-step reasoning)
4. **Pause before any destructive action** (restart, rollback) and ask for human approval
5. Maintain full conversation state across interruptions

**Starter file:** `starter/langgraph_agent.py`

---

## Quiz

1. What is the difference between a LangGraph `State` and a regular Python dict?
2. What does a "checkpoint" enable in LangGraph? Give a real-world use case.
3. How do conditional edges work? When would you use one vs. a fixed edge?
