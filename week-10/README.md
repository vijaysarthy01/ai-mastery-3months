# Week 10: Agent Reliability + Observability

## Goal
Most AI agents fail in production due to unpredictable LLM outputs, latency, and cost. Learn to make your agents production-ready.

---

## Watch + Build (free)

| Resource | URL |
|----------|-----|
| Nvidia's NeMo: Making Agents Reliable | https://www.deeplearning.ai/short-courses/nvidia-nat-making-agents-reliable/ |
| Semantic Caching for AI Agents | https://www.deeplearning.ai/short-courses/semantic-caching-for-ai-agents/ |
| LangSmith (observability) | https://docs.smith.langchain.com/ |

---

## Key Concepts

```
Tracing         — Record every LLM call: input, output, latency, tokens, cost
Semantic Cache  — Cache responses by meaning (not exact text), so "fix the bug" and
                  "repair the issue" return the same cached answer
Retry Logic     — Handle rate limits and transient API errors gracefully
Output Validation — Verify LLM output matches expected format before using it
Fallback Models — If claude-sonnet-4-6 fails, fall back to claude-haiku-4-5
```

---

## Build Assignment

**Take your Week 6 or Week 9 agent and make it production-ready.**

Add these reliability features:
1. **Tracing**: Log every LLM call to a JSON file (input, output, duration, tokens)
2. **Retry with backoff**: Handle `anthropic.RateLimitError` and `anthropic.APIStatusError`
3. **Semantic caching**: Cache responses in ChromaDB; return cached answer if similarity > 0.95
4. **Output validation**: Verify JSON outputs match expected schema before using them
5. **Cost tracking**: Track and display cumulative token usage and estimated cost

**Starter file:** `starter/reliable_agent.py`

---

## Quiz

1. What is the difference between semantic caching and exact-match caching?
2. What exponential backoff strategy should you use for API rate limits?
3. Name 3 things you should trace in every LLM call for production observability.
