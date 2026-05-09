# Week 9: Multi-Agent Systems with CrewAI

## Goal
Build a team of specialized AI agents that collaborate to solve complex problems. This is the state of the art in production AI systems.

---

## Watch + Build (free)

| Resource | URL |
|----------|-----|
| Multi AI Agent Systems with crewAI | https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/ |
| CrewAI Docs | https://docs.crewai.com/ |

---

## Key CrewAI Concepts

```
Agent       — A specialized LLM worker with a role, goal, and tools
Task        — A job assigned to an Agent with expected output format
Crew        — A team of Agents + Tasks + execution strategy
Process     — Sequential (one after another) or Hierarchical (manager delegates)
```

---

## Build Assignment

**Build a 3-agent DevOps incident response pipeline.**

| Agent | Role | Responsibility |
|-------|------|---------------|
| Monitor Agent | Log Analyzer | Reads logs, identifies anomalies, extracts error patterns |
| Diagnosis Agent | Root Cause Analyst | Takes Monitor's output, diagnoses root cause with reasoning |
| Reporter Agent | Incident Reporter | Writes a formatted incident report from Monitor + Diagnosis output |

The three agents run **sequentially** — each passes its output to the next.

**Starter file:** `starter/crew_pipeline.py`

---

## Quiz

1. What is the difference between `Process.sequential` and `Process.hierarchical` in CrewAI?
2. How do CrewAI agents share information between tasks?
3. When would you use CrewAI vs. LangGraph for a multi-agent system?
