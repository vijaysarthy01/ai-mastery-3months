# Week 2: Prompt Engineering

## Goal
Go beyond "just ask Claude something." Learn to engineer prompts that produce consistent, structured, reliable output — the foundation of every AI application.

---

## Watch (3 hrs)

| Resource | URL | Focus |
|----------|-----|-------|
| ChatGPT Prompt Engineering for Developers | https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/ | Full course (1.5 hrs) |
| Anthropic Prompt Engineering Guide | https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview | Read the full guide |

---

## Key Concepts

| Technique | What It Does | When to Use |
|-----------|-------------|-------------|
| **Zero-shot** | No examples, just instruction | Simple, clear tasks |
| **Few-shot** | 2-5 examples before the task | Tasks needing consistent format |
| **Chain-of-thought** | Ask Claude to "think step by step" | Reasoning, math, analysis |
| **System prompt** | Sets Claude's persona/role | Every production application |
| **Output format control** | Ask for JSON, bullet points, XML | When you need to parse the output |

---

## Build Assignment

**Build a dynamic prompt template system in Python.**

The system should:
1. Define at least 3 task types: `summarize`, `classify`, `extract`
2. For each task type, build the correct prompt using few-shot examples
3. Accept user input (text + task type) and return the result
4. Parse structured output (JSON) from Claude

**Starter file:** `starter/prompt_templates.py`

---

## Quiz (answer before moving to Week 3)

1. What is the difference between a **system prompt** and a **user message**? Why does the distinction matter?
2. When should you use few-shot prompting instead of zero-shot? Give a concrete example.
3. How do you reliably get Claude to return JSON? What can go wrong?
