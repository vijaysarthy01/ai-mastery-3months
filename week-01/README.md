# Week 1: Python for AI Engineers

## Goal
Write Python fluently enough to call the Claude API and process its responses programmatically.

> You know Java. Python is similar but simpler. Focus on the 20% of Python that covers 80% of AI development.

---

## Watch (3 hrs)

| Resource | URL | Focus |
|----------|-----|-------|
| Python for Everybody | https://www.py4e.com/lessons | Chapters 1-9 only |
| Anthropic API Quickstart | https://docs.anthropic.com/en/api/getting-started | Read fully |
| Claude Models Overview | https://docs.anthropic.com/en/docs/about-claude/models/overview | Know the model names |

---

## Build Assignment

**Build a CLI text summarizer using the Claude API.**

The program should:
1. Accept a text file path as a command-line argument
2. Read the file contents
3. Send the contents to Claude claude-sonnet-4-6 with a summarization prompt
4. Print the summary to the terminal

**Starter file:** `starter/summarizer.py`

Run it like this:
```bash
python starter/summarizer.py my_document.txt
```

---

## Key Python Concepts You Need This Week

```python
# 1. Reading files
with open("file.txt", "r") as f:
    content = f.read()

# 2. Command-line args
import sys
filename = sys.argv[1]

# 3. Environment variables (never hardcode API keys!)
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

# 4. The Anthropic SDK
import anthropic
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
print(message.content[0].text)
```

---

## Quiz (answer before moving to Week 2)

1. What is the difference between `sys.argv` and `argparse`? When would you use each?
2. Why should you never hardcode your API key directly in a Python file?
3. In the Anthropic SDK, what does `max_tokens` control? What happens if you set it too low?

---

## Done? Checkpoint

- [ ] My summarizer runs on a real text file
- [ ] I used `python-dotenv` to load my API key from `.env`
- [ ] I pushed my solution to `solution/summarizer.py`
- [ ] I can answer all 3 quiz questions above
