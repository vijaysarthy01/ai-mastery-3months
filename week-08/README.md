# Week 8: Agent Memory Systems

## Goal
Build agents that remember. Stateless agents are useless in production — they forget every conversation. Learn to implement all 4 types of agent memory.

---

## Watch + Build (free)

| Resource | URL |
|----------|-----|
| Agent Memory: Building Memory-Aware Agents | https://www.deeplearning.ai/short-courses/agent-memory-building-memory-aware-agents/ |

---

## The 4 Types of Agent Memory

| Type | What It Stores | Where | Example |
|------|---------------|-------|---------|
| **In-Context** | Current conversation | Prompt (RAM) | "Earlier you said the API is down" |
| **External** | Long-term facts | Database/files | Team preferences, past incidents |
| **Episodic** | What happened in past sessions | ChromaDB/JSON | "Last Tuesday we had a similar issue" |
| **Semantic** | General knowledge/rules | Embedding store | "P1 incidents require war room within 10 min" |

---

## Build Assignment

**Build a memory-aware DevOps assistant that remembers your team and past incidents.**

The assistant should:
1. Remember team member names and their specialties (external memory)
2. Recall past incidents when a similar issue arises (episodic memory)
3. Know your team's runbook rules (semantic memory via ChromaDB)
4. Maintain conversation context within a session (in-context memory)

After each conversation, save new incidents to the memory store.

**Starter file:** `starter/memory_agent.py`

---

## Quiz

1. What is the difference between episodic memory and semantic memory in agents?
2. Why can't you just put everything in the context window instead of external memory?
3. How do you decide what memories are worth saving vs. what should be discarded?
