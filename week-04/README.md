# Week 4: RAG — Retrieval Augmented Generation

## Goal
Build a Q&A bot that answers questions from your own documents. This is the foundation of enterprise AI — connecting LLMs to private knowledge.

---

## Watch (3 hrs)

| Resource | URL | Focus |
|----------|-----|-------|
| Building Systems with the ChatGPT API | https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/ | Full course |
| ChromaDB Docs | https://docs.trychroma.com/getting-started | Quickstart section |

---

## Key Concepts

```
Embedding       — Converts text into a vector (list of numbers) representing its meaning
Vector Store    — A database that stores and searches embeddings (we use ChromaDB)
Similarity Search — Find documents whose meaning is closest to the query
RAG Pipeline    — 1) Embed documents → 2) Embed query → 3) Find similar docs → 4) Pass to LLM
Chunking        — Split large documents into smaller pieces before embedding
```

## How RAG Works

```
Your Documents → Split into Chunks → Embed each Chunk → Store in ChromaDB
                                                              ↓
User Question → Embed Question → Search ChromaDB → Top 3 Chunks
                                                              ↓
                            Claude + Question + Top 3 Chunks → Answer
```

---

## Build Assignment

**Build a Q&A bot over your own documents.**

The app should:
1. Load `.txt` files from a `docs/` folder
2. Split them into chunks (500 chars with 50 char overlap)
3. Store chunks in ChromaDB with embeddings
4. Accept a question from the user
5. Find the 3 most relevant chunks
6. Pass chunks + question to Claude and return an answer

**Starter file:** `starter/rag_bot.py`

Create a `docs/` folder with 2-3 text files — use your team's runbooks, documentation, or any work content.

---

## Quiz

1. What problem does RAG solve that fine-tuning does not?
2. What is "chunking" and why does chunk size matter?
3. What happens if the answer to a user's question is not in any of your documents?
