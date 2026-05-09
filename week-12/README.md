# Week 12: Capstone — DevOps AI Assistant

## Goal
Build and demo a complete, production-ready DevOps AI Assistant that integrates everything from the past 11 weeks.

---

## This Is Your Portfolio Piece

This project demonstrates to any engineering organization that you can:
- Design and build multi-agent AI systems
- Connect AI agents to real tools via MCP
- Implement persistent memory and observability
- Build with production reliability standards
- Lead AI development, not just manage it

---

## System Architecture

```
User (CLI or Claude Desktop)
        ↓
Orchestrator Agent
        ├─── Monitor Agent      → Analyzes logs, detects anomalies
        ├─── Diagnosis Agent    → Root cause analysis
        ├─── Action Agent       → Plans remediation steps
        └─── Reporter Agent     → Writes incident report

Each agent has:
  - Persistent memory (ChromaDB)
  - MCP tools (kubectl, logs, tickets)
  - Human-in-the-loop for destructive actions
  - Full tracing + cost tracking
```

---

## What You Are Building

A CLI application where an engineer types:

```
> payment-api is returning 503 errors since 2:30pm UTC
```

And the system:
1. **Orchestrator** receives the incident, routes to specialist agents
2. **Monitor Agent** analyzes logs (via MCP tool), identifies error pattern
3. **Diagnosis Agent** determines root cause (DB connection pool exhaustion)
4. **Action Agent** proposes remediation → pauses for human approval
5. **Reporter Agent** generates a formal incident report
6. Everything is traced, cached, and saved to memory for future reference

---

## Requirements

| Feature | Week Learned |
|---------|-------------|
| Claude API (streaming, multi-turn) | Week 3 |
| Prompt engineering (system prompts, structured output) | Week 2 |
| RAG for runbook knowledge | Week 4 |
| Agent patterns (routing, orchestrator-workers) | Week 5 |
| LangGraph state management | Week 6 |
| MCP tools (kubectl, logs, tickets) | Week 7 |
| Persistent memory (episodic + semantic) | Week 8 |
| Multi-agent CrewAI or custom | Week 9 |
| Reliability (retry, caching, tracing) | Week 10 |

---

## Starter File

`starter/devops_agent.py` — Architecture scaffold with all components stubbed out.

---

## Demo Checklist (present to your team)

- [ ] Show the full incident flow end-to-end
- [ ] Show a second identical incident is answered faster (semantic cache hit)
- [ ] Show past incident recall (episodic memory)
- [ ] Show human approval gate before a service restart
- [ ] Show the trace log and token cost summary
- [ ] Walk through the architecture diagram above

---

## Congratulations

If you reach this point, you have:

- Built 12 real Python AI projects
- Mastered the Claude API, LangGraph, MCP, CrewAI
- Built and shipped a production-grade multi-agent system
- A GitHub portfolio that proves you can build, not just manage

**You are ready for the AI Development Manager role.**

---

## Next Steps (Beyond Week 12)

| Topic | Resource |
|-------|----------|
| Fine-tuning Claude | https://docs.anthropic.com/en/docs/build-with-claude/fine-tuning |
| Agent Skills with Anthropic | https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/ |
| Building Coding Agents | https://www.deeplearning.ai/short-courses/building-coding-agents-with-tool-execution/ |
| Deploy agents with LangGraph Cloud | https://langchain-ai.github.io/langgraph/cloud/ |
