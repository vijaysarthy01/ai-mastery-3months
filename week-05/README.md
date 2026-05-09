# Week 5: Anthropic Agent Patterns

## Goal
Implement the 4 core agentic patterns defined by Anthropic's research team. These are the building blocks of every production AI agent system.

---

## Read (mandatory — this is Anthropic's research, not opinion)

| Resource | URL |
|----------|-----|
| Building Effective Agents | https://www.anthropic.com/research/building-effective-agents |

Read the entire article. Take notes on each pattern.

---

## The 4 Patterns You Will Implement

### 1. Prompt Chaining
Break a complex task into sequential steps. Output of step N is input to step N+1.
```
User Request → [Step 1: Plan] → [Step 2: Draft] → [Step 3: Review] → Final Output
```

### 2. Routing
Classify the input and route to the appropriate handler.
```
User Request → [Classifier] → Route A (simple) or Route B (complex) or Route C (escalate)
```

### 3. Orchestrator-Workers
A central LLM breaks down a task and delegates to specialized workers in parallel.
```
User Request → [Orchestrator: plan subtasks] → [Worker A] [Worker B] [Worker C] → Aggregate
```

### 4. Evaluator-Optimizer
Generate output, then evaluate it, then refine in a loop until quality threshold is met.
```
User Request → [Generator] → [Evaluator: score 1-10] → if score < 8: [Refine] → repeat
```

---

## Build Assignment

Implement each pattern as a standalone Python function in `starter/agent_patterns.py`.

Use a **DevOps incident report** as the test case — it's directly relevant to your work.

---

## Quiz

1. Anthropic says "start simple." What does that mean practically when building an agent?
2. When would you choose Orchestrator-Workers over Prompt Chaining?
3. What is the risk of the Evaluator-Optimizer pattern in production? How do you mitigate it?
