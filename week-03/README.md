# Week 3: Claude API Deep Dive

## Goal
Master the full Claude API: multi-turn conversations, streaming, system prompts, token management, and model selection.

---

## Watch / Read (3 hrs)

| Resource | URL | Focus |
|----------|-----|-------|
| Anthropic API Reference | https://docs.anthropic.com/en/api/getting-started | Messages API |
| Claude Models Overview | https://docs.anthropic.com/en/docs/about-claude/models/overview | When to use which model |
| Streaming Guide | https://docs.anthropic.com/en/api/messages-streaming | Streaming responses |

---

## Key Concepts

```
Context window   — How much text Claude can "see" at once (200K tokens for claude-sonnet-4-6)
max_tokens       — Maximum tokens in Claude's response (not input)
Multi-turn       — Sending conversation history so Claude remembers context
Streaming        — Getting response word-by-word instead of waiting for full reply
Temperature      — Controls randomness (0 = deterministic, 1 = creative)
```

---

## Build Assignment

**Build a multi-turn streaming chat application.**

The app should:
1. Keep a conversation history in memory (list of messages)
2. Stream Claude's responses to the terminal in real-time (word by word)
3. Let the user type "quit" to exit
4. Show a token count after each response
5. Have a configurable system prompt (e.g., "You are a DevOps expert assistant")

**Starter file:** `starter/chat_app.py`

---

## Quiz

1. What is a "context window"? What happens when a conversation exceeds it?
2. What is the difference between `claude-haiku-4-5` and `claude-sonnet-4-6`? When would you use each?
3. Why is streaming better for user experience? What changes in the API call?
