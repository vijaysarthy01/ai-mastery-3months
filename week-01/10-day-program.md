# 10-Day Python to AI Agent Mastery Program

---

## Program Architecture

**Total Time:** 10 days × 3 hours = 30 hours
**Learning Methods Used:**
- **Active Recall** (Ebbinghaus, 1885) — quizzes at end of each session
- **Spaced Repetition** (Cepeda et al., 2006) — daily review of prior day's key concepts (15 min built in)
- **Project-Based Learning** (Krajcik & Shin, 2014) — every day ends with a mini-build
- **Interleaving** (Rohrer & Taylor, 2007) — concepts mixed across days, not siloed
- **Desirable Difficulty** (Bjork, 1994) — intentional challenge that slightly exceeds comfort zone

---

## The 3-Phase Structure

```
Phase 1 (Days 1-3): Python Foundations
Phase 2 (Days 4-7): AI Tooling & API Mastery
Phase 3 (Days 8-10): Agent Development & Deployment
```

---

## Phase 1 — Python Foundations

---

### Day 1 — Variables, Logic, and Your First Python Program

**Theme:** "You are teaching the computer how to think."

#### Hour 1 — Concepts (60 min)

**Start with Why (5 min):**
Before code, understand this: Python is just a precise way to give instructions. You already give instructions every day — a recipe, directions, a to-do list. Python is the same, but for computers.

**Core Concepts:**

```python
# Variables — containers for information
name = "Alex"
age = 25
is_learning = True
score = 98.5

# Python is dynamically typed — it figures out the type for you
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(score))   # <class 'float'>
print(type(is_learning))  # <class 'bool'>
```

```python
# String operations — working with text
greeting = "Hello, " + name        # concatenation
message = f"My name is {name} and I am {age} years old."  # f-strings (preferred)
print(message.upper())             # HELLO...
print(len(message))                # character count
print(message.replace("Alex", "Sam"))
```

```python
# Basic math
total = 10 + 5      # 15
difference = 10 - 3 # 7
product = 4 * 6     # 24
quotient = 15 / 4   # 3.75 (always float)
floor_div = 15 // 4 # 3   (integer division)
remainder = 15 % 4  # 3   (modulo — very useful)
power = 2 ** 8      # 256
```

```python
# Conditionals — decision making
temperature = 85

if temperature > 90:
    print("Stay inside — too hot!")
elif temperature > 70:
    print("Perfect weather for coding outside.")
else:
    print("Grab a jacket.")

# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
if temperature > 70 and temperature < 90:
    print("Goldilocks zone.")
```

#### Hour 2 — Loops and Functions (60 min)

```python
# Loops — repetition without rewriting
# For loop — when you know how many times
for i in range(5):          # 0, 1, 2, 3, 4
    print(f"Step {i}")

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(f"Count: {i}")

# While loop — when you loop until a condition is false
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1              # CRITICAL: always increment or you get infinite loop

# Loop control
for i in range(10):
    if i == 5:
        break               # stop the loop entirely
    if i % 2 == 0:
        continue            # skip this iteration, go to next
    print(i)                # prints 1, 3
```

```python
# Functions — reusable blocks of logic
# Think of functions as your own custom commands

def greet(person_name):
    return f"Hello, {person_name}!"

# Call the function
message = greet("Alex")
print(message)  # Hello, Alex!

# Functions with multiple parameters and a default value
def calculate_score(correct, total, bonus=0):
    percentage = (correct / total) * 100
    return percentage + bonus

print(calculate_score(8, 10))       # 80.0
print(calculate_score(8, 10, 5))    # 85.0
```

```python
# IMPORTANT: Functions as first-class objects (preview of AI concepts)
# In Python, functions can be stored in variables and passed around
def double(x):
    return x * 2

def triple(x):
    return x * 3

# Store in a variable
my_function = double
print(my_function(5))   # 10

# This concept is CORE to how AI agents work — later you'll pass
# functions to AI models as "tools"
```

#### Hour 3 — Build: Personal Study Tracker (60 min)

```python
# Build a simple CLI study tracker
# File: study_tracker.py

def add_topic(topics, topic_name, hours_studied):
    topics[topic_name] = topics.get(topic_name, 0) + hours_studied
    print(f"Logged {hours_studied}h for {topic_name}. Total: {topics[topic_name]}h")
    return topics

def show_progress(topics):
    if not topics:
        print("No topics logged yet.")
        return

    print("\n=== Study Progress ===")
    total = 0
    for topic, hours in topics.items():
        bar = "█" * int(hours)
        print(f"{topic:20} | {bar} {hours}h")
        total += hours
    print(f"\nTotal study time: {total}h")

def recommend_review(topics):
    print("\n=== Recommended for Review ===")
    for topic, hours in topics.items():
        if hours < 2:
            print(f"  {topic} — needs more time (only {hours}h logged)")

def main():
    topics = {}

    while True:
        print("\n1. Log study session")
        print("2. View progress")
        print("3. Get review recommendations")
        print("4. Quit")

        choice = input("\nChoose (1-4): ")

        if choice == "1":
            topic = input("Topic name: ")
            hours = float(input("Hours studied: "))
            topics = add_topic(topics, topic, hours)
        elif choice == "2":
            show_progress(topics)
        elif choice == "3":
            recommend_review(topics)
        elif choice == "4":
            print("Keep learning! Consistency beats intensity.")
            break
        else:
            print("Invalid choice. Try again.")

main()
```

**Active Recall Quiz — Day 1:**
1. What is the difference between `=` and `==`?
2. What does `%` (modulo) return?
3. Why must a `while` loop have an increment?
4. What does `return` do in a function vs `print`?
5. What will `range(2, 10, 3)` produce?

*Answers: (1) assignment vs comparison, (2) remainder after division, (3) prevent infinite loop, (4) return gives value back to caller; print just displays, (5) 2, 5, 8*

---

### Day 2 — Data Structures: Lists, Dicts, and Thinking in Collections

**Theme:** "AI systems are built on organizing and transforming data."

**Day Review (15 min):** Before starting, write from memory: what are the 4 variable types? What does a function need to be useful?

#### Hour 1 — Lists (60 min)

```python
# Lists — ordered, changeable collections
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [42, "hello", True, 3.14]

# Indexing — positions start at 0
print(fruits[0])    # apple
print(fruits[-1])   # cherry (negative = from end)
print(fruits[1:3])  # ['banana', 'cherry'] (slicing)

# Mutating lists
fruits.append("date")
fruits.insert(1, "avocado")
fruits.remove("banana")
popped = fruits.pop()
fruits.pop(0)

# Useful list operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numbers))
numbers.sort()
print(len(numbers))
print(sum(numbers))
print(min(numbers), max(numbers))
print(5 in numbers)
```

```python
# List comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Real use case: clean a list of AI responses
responses = ["  Hello  ", "World\n", " AI is cool "]
cleaned = [r.strip() for r in responses]
```

#### Hour 2 — Dictionaries and Tuples (60 min)

```python
# Dictionaries — key-value pairs
person = {
    "name": "Alex",
    "age": 25,
    "skills": ["Python", "Logic", "Problem-solving"],
    "is_active": True
}

# Access
print(person["name"])
print(person.get("salary", 0))   # safe default if key missing

# Modify
person["age"] = 26
person["location"] = "New York"
del person["is_active"]

# Iterate
for key, value in person.items():
    print(f"{key}: {value}")
```

```python
# Why dicts are crucial for AI: API responses are dicts
ai_response = {
    "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
    "type": "message",
    "role": "assistant",
    "content": [{"type": "text", "text": "Hello! I'm Claude."}],
    "model": "claude-sonnet-4-6",
    "usage": {"input_tokens": 10, "output_tokens": 8}
}

text = ai_response["content"][0]["text"]
input_tokens = ai_response["usage"]["input_tokens"]
```

```python
# Tuples — immutable lists
coordinates = (40.7128, -74.0060)
lat, lon = coordinates   # unpacking

def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9])
```

#### Hour 3 — Build: Conversation Memory System (60 min)

```python
# Mirrors how real AI chatbots store context

def create_conversation():
    return {"messages": [], "total_turns": 0, "word_count": 0}

def add_message(conversation, role, content):
    message = {
        "role": role,
        "content": content,
        "turn": conversation["total_turns"] + 1
    }
    conversation["messages"].append(message)
    conversation["total_turns"] += 1
    conversation["word_count"] += len(content.split())
    return conversation

def get_context_window(conversation, last_n=5):
    """Return last N messages — this is how real AI context windows work"""
    return conversation["messages"][-last_n:]

def search_conversation(conversation, keyword):
    return [
        msg for msg in conversation["messages"]
        if keyword.lower() in msg["content"].lower()
    ]
```

**Active Recall Quiz — Day 2:**
1. What's the difference between `list.sort()` and `sorted(list)`?
2. How do you safely access a dict key that might not exist?
3. Why can't you modify a tuple?
4. What is `list[-2]`?
5. Write a list comprehension that squares only odd numbers from 1-20.

---

### Day 3 — Object-Oriented Programming and File I/O

**Theme:** "OOP is how you model real-world entities. AI agents ARE objects."

**Day Review (15 min):** From memory: what's the difference between a list and a dict? When would you use each?

#### Hour 1 — Classes and Objects (60 min)

```python
class AIAgent:
    agent_count = 0

    def __init__(self, name, model, temperature=0.7):
        self.name = name
        self.model = model
        self.temperature = temperature
        self.conversation_history = []
        self.total_tokens_used = 0
        AIAgent.agent_count += 1

    def add_to_history(self, role, content):
        self.conversation_history.append({"role": role, "content": content})

    def get_system_prompt(self):
        return f"You are {self.name}, a helpful AI assistant."

    def reset(self):
        self.conversation_history = []
        print(f"{self.name}: Memory cleared.")

    def status(self):
        print(f"\n=== Agent: {self.name} ===")
        print(f"Model: {self.model}")
        print(f"Temperature: {self.temperature}")
        print(f"Messages in history: {len(self.conversation_history)}")

    def __str__(self):
        return f"AIAgent({self.name}, model={self.model})"
```

```python
# Inheritance
class SpecializedAgent(AIAgent):
    def __init__(self, name, model, domain, tools=None):
        super().__init__(name, model)
        self.domain = domain
        self.tools = tools or []

    def get_system_prompt(self):
        base_prompt = super().get_system_prompt()
        return f"{base_prompt} You specialize in {self.domain}."

    def add_tool(self, tool_name):
        self.tools.append(tool_name)
        print(f"{self.name}: Tool '{tool_name}' added.")
```

#### Hour 2 — File I/O and Error Handling (60 min)

```python
import json
import os

# Writing and reading files
with open("notes.txt", "w") as f:
    f.write("Day 3 of AI learning\n")

with open("notes.txt", "a") as f:
    f.write("Progress: Excellent!\n")

with open("notes.txt", "r") as f:
    content = f.read()
```

```python
# JSON — the language of APIs
conversation_data = {
    "agent": "Helper",
    "model": "claude-sonnet-4-6",
    "messages": [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi!"}
    ]
}

with open("conversation.json", "w") as f:
    json.dump(conversation_data, f, indent=2)

with open("conversation.json", "r") as f:
    loaded_data = json.load(f)
```

```python
# Error handling
def safe_read_json(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}")
        return {}
    finally:
        print("File operation attempted.")

# Custom exceptions
class TokenLimitError(Exception):
    def __init__(self, tokens_used, limit):
        super().__init__(f"Token limit exceeded: {tokens_used} > {limit}")
```

#### Hour 3 — Build: Persistent Agent State Manager (60 min)

```python
import json
import os
from datetime import datetime

class AgentMemory:
    def __init__(self, agent_name, storage_dir="./agent_memories"):
        self.agent_name = agent_name
        self.storage_dir = storage_dir
        self.filepath = os.path.join(storage_dir, f"{agent_name}.json")
        self.data = self._load()

    def _load(self):
        os.makedirs(self.storage_dir, exist_ok=True)
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        return {
            "agent_name": self.agent_name,
            "created_at": datetime.now().isoformat(),
            "messages": [],
            "metadata": {}
        }

    def save(self):
        self.data["last_updated"] = datetime.now().isoformat()
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=2)

    def add_message(self, role, content):
        self.data["messages"].append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        self.save()

    def get_recent(self, n=10):
        return self.data["messages"][-n:]

    def search(self, keyword):
        return [
            m for m in self.data["messages"]
            if keyword.lower() in m["content"].lower()
        ]

    def stats(self):
        msgs = self.data["messages"]
        user_msgs = [m for m in msgs if m["role"] == "user"]
        return {
            "total_messages": len(msgs),
            "user_messages": len(user_msgs),
            "assistant_messages": len(msgs) - len(user_msgs),
        }
```

**Active Recall Quiz — Day 3:**
1. What is `__init__` and when does it run?
2. What does `super().__init__()` do?
3. What is the difference between `json.dump` and `json.dumps`?
4. Why use `with open(...)` instead of `f = open(...)`?
5. What is the purpose of `finally` in a try/except block?

---

## Phase 2 — AI Tooling and API Mastery

---

### Day 4 — Python Advanced Patterns + Environment Setup

**Theme:** "Professional Python before we touch any AI API."

**Day Review (15 min):** Without looking, write a class with `__init__`, one method, and inheritance.

#### Hour 1 — Modules, Virtual Environments, Package Management (60 min)

```bash
# Create and activate a virtual environment
python -m venv ai_learning_env
source ai_learning_env/bin/activate     # Mac/Linux
ai_learning_env\Scripts\activate        # Windows

# Install packages
pip install anthropic openai requests python-dotenv

# Save dependencies
pip freeze > requirements.txt
```

```python
# Environment variables — store secrets safely
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY not set in .env file")
```

#### Hour 2 — Advanced Python for AI (60 min)

```python
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.3f}s")
        return result
    return wrapper

def retry(max_attempts=3, delay=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt+1} failed: {e}. Retrying...")
                    time.sleep(delay * (attempt + 1))
        return wrapper
    return decorator

@timer
@retry(max_attempts=3)
def call_ai_api(prompt):
    time.sleep(0.1)
    return f"Response to: {prompt}"
```

```python
# Generators — used in streaming AI responses
def stream_tokens(text):
    for word in text.split():
        yield word
        time.sleep(0.05)

for token in stream_tokens("Hello world this is streaming output"):
    print(token, end=" ", flush=True)
```

#### Hour 3 — Build: Project Scaffolding for AI Apps (60 min)

Recommended project structure for all future AI projects:

```
ai_agent_project/
├── .env                    # API keys (never commit)
├── .gitignore
├── requirements.txt
├── main.py
├── agents/
│   ├── __init__.py
│   └── base_agent.py
├── tools/
│   ├── __init__.py
│   └── web_search.py
├── memory/
│   ├── __init__.py
│   └── conversation.py
└── tests/
    └── test_agents.py
```

---

### Day 5 — Your First Real AI API Call

**Theme:** "The gap between understanding AI and building with AI is one API call."

**Day Review (15 min):** What is a decorator? What is a virtual environment for?

#### Hour 1 — HTTP Requests and API Concepts (60 min)

```python
import requests

# GET request
response = requests.get("https://api.github.com/users/anthropics")
print(response.status_code)   # 200 = success
data = response.json()

# POST request
payload = {"title": "Test", "body": "Content", "userId": 1}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload,
    headers={"Authorization": "Bearer fake_token"}
)

# HTTP Status Codes:
# 200 OK, 201 Created
# 400 Bad Request, 401 Unauthorized
# 429 Too Many Requests (rate limited)
# 500 Internal Server Error
```

#### Hour 2 — Claude API Integration (60 min)

```python
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Basic API call
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Explain recursion in 2 sentences."}]
)
print(response.content[0].text)
print(f"Tokens: {response.usage.input_tokens} in / {response.usage.output_tokens} out")
```

```python
# Multi-turn conversations
def chat_with_claude(conversation_history, user_message, system_prompt=None):
    conversation_history.append({"role": "user", "content": user_message})

    kwargs = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 1024,
        "messages": conversation_history
    }
    if system_prompt:
        kwargs["system"] = system_prompt

    response = client.messages.create(**kwargs)
    assistant_message = response.content[0].text
    conversation_history.append({"role": "assistant", "content": assistant_message})

    return assistant_message, conversation_history
```

```python
# Streaming responses
def stream_response(prompt, system=None):
    kwargs = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": prompt}]
    }
    if system:
        kwargs["system"] = system

    print("Claude: ", end="", flush=True)
    with client.messages.stream(**kwargs) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
    print()
```

#### Hour 3 — Build: Interactive AI Tutor CLI (60 min)

See `starter/tutor.py` for the full implementation.

---

### Day 6 — Tool Use and Function Calling

**Theme:** "Tools are what transform a chatbot into an agent."

**Day Review (15 min):** What is `max_tokens`? What is a system prompt? What is streaming?

#### The Agentic Loop

```
1. User sends message
2. Claude decides a tool is needed
3. Claude returns a "tool_use" block (not text)
4. Your code executes the actual tool
5. You send the tool result back to Claude
6. Claude uses the result to form a final answer
```

#### Hour 1 — Defining Tools (60 min)

```python
TOOLS = [
    {
        "name": "calculator",
        "description": "Performs mathematical calculations.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to evaluate"
                }
            },
            "required": ["expression"]
        }
    }
]

import math

def calculator(expression: str) -> str:
    try:
        allowed = {"sqrt": math.sqrt, "pi": math.pi, "abs": abs, "round": round}
        result = eval(expression, {"__builtins__": {}}, allowed)
        return str(result)
    except Exception as e:
        return f"Error: {e}"
```

#### Hour 2 — The Agentic Loop (60 min)

```python
def run_agent(user_message, tools, tool_map, system=None):
    messages = [{"role": "user", "content": user_message}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system or "You are a helpful assistant with access to tools.",
            tools=tools,
            messages=messages
        )

        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text

        elif response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    func = tool_map.get(block.name)
                    result = func(**block.input) if func else "Tool not found"
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            messages.append({"role": "user", "content": tool_results})
```

#### Hour 3 — Build: Research Agent with Wikipedia Tool (60 min)

See `starter/research_agent.py` for the full implementation.

---

### Day 7 — Prompt Engineering Mastery

**Theme:** "Prompt engineering is the craft of communicating with AI systems precisely."

**Day Review (15 min):** Draw from memory the agentic loop.

#### Core Techniques

**1. Zero-Shot vs Few-Shot (Brown et al., 2020)**
```python
# Few-shot — teach by example
few_shot = """Classify sentiment: POSITIVE, NEGATIVE, or NEUTRAL.

Review: "Best purchase ever!" → POSITIVE
Review: "It works, nothing special." → NEUTRAL
Review: "Broke after one day." → NEGATIVE

Review: "This is absolutely terrible." →"""
```

**2. Chain of Thought (Wei et al., 2022)**
```python
# Add "Let's think step by step:" to improve accuracy on complex tasks
prompt = "Roger has 5 balls. He buys 2 cans of 3 each. How many total?\n\nLet's think step by step:"
```

**3. ReAct Pattern (Yao et al., 2022)**
```
Thought: [reasoning]
Action: [what to do]
Observation: [result]
... repeat until Final Answer
```

**4. Structured Output**
```python
prompt = """Analyze this idea and return ONLY valid JSON:
{
  "score": <1-10>,
  "pros": [<3 items>],
  "cons": [<3 items>],
  "recommendation": <"build"|"research"|"skip">
}"""
```

**5. Self-Critique Pipeline**
```python
# Generate → Critique → Improve
initial = prompt(task)
critique = prompt(f"Critique this response: {initial}")
improved = prompt(f"Improve based on critique: {critique}")
```

#### Hour 3 — Build: Prompt Engineering Workbench (60 min)

See `starter/prompt_workbench.py` — a tool to A/B test different prompting strategies.

---

## Phase 3 — Agent Development and Deployment

---

### Day 8 — Multi-Agent Systems and Orchestration

**Theme:** "One agent is a tool. Multiple agents collaborating is a system."

**Day Review (15 min):** What is the agentic loop? What is the ReAct pattern?

#### Orchestrator Pattern

```python
class Agent:
    def __init__(self, name, system_prompt, tools=None, model="claude-sonnet-4-6"):
        self.name = name
        self.system_prompt = system_prompt
        self.tools = tools or []
        self.model = model

    def run(self, message, tool_map=None):
        # Full agentic loop implementation
        ...

class OrchestratorAgent:
    """Breaks tasks into subtasks and delegates to specialists"""
    def __init__(self, specialists):
        self.specialists = specialists

    def run(self, user_request):
        # 1. Plan (orchestrator → JSON plan)
        # 2. Execute (route to specialists)
        # 3. Compile (merge results)
        ...
```

#### Specialist Roles

| Specialist | System Prompt Focus |
|-----------|---------------------|
| Researcher | Key facts, nuances, what reader needs to know |
| Writer | Engaging prose, inverted pyramid, 8th-grade reading |
| Editor | Clarity, flow, factual checks, headline |
| SEO Analyst | Keywords, meta description, SEO score |

#### Hour 3 — Build: Customer Support Agent System (60 min)

See `starter/support_system.py` — multi-agent support bot with order lookup, product info, and ticket creation tools.

---

### Day 9 — Agentic Patterns and Real-World Architecture

**Theme:** "Production AI systems need more than clever prompts — they need architecture."

#### Hour 1 — Evaluation and Guardrails (60 min)

```python
class AgentEvaluator:
    def evaluate_response(self, question, response):
        """Rate on: accuracy, helpfulness, clarity, safety (1-5 each)"""
        ...

    def check_safety(self, user_input):
        """Return: is_safe, risk_level, concerns, recommended_action"""
        ...

    def run_test_suite(self, agent_func, test_cases):
        """Run battery of tests, return average score"""
        ...
```

#### Hour 2 — Caching, Rate Limiting, Cost Management (60 min)

```python
class CachedAIClient:
    """Cache responses to reduce cost and latency"""
    # MD5 hash of (messages + system) as cache key
    # TTL-based expiry
    # Track: hits, misses, cost saved

class RateLimiter:
    """Token bucket algorithm — prevent 429 errors"""
    # min_interval = 60 / requests_per_minute
    # sleep if last request was too recent
```

**Approximate Claude Sonnet pricing:**
- Input: $3 per million tokens
- Output: $15 per million tokens

#### Hour 3 — Build: Complete AI Pipeline (60 min)

```python
class ProductionAgent:
    """
    Production-grade agent with:
    - Persistent memory
    - Tool use with error recovery
    - Usage tracking
    - Input validation
    - Automatic retry on rate limits
    - Max iteration guard
    """
    def chat(self, user_input, max_tool_iterations=10):
        # Full agentic loop with all safeguards
        ...
```

---

### Day 10 — Capstone Project + Career Launch

**Theme:** "Build something real. Share it. Get hired."

#### Capstone Options (pick one)

**Option A: Personal AI Assistant**
- Persistent memory, web search, code execution, calendar awareness

**Option B: AI Content Pipeline**
- Multi-agent: Research → Outline → Write → Edit → Format
- Input: topic + target audience; Output: complete blog post

**Option C: AI Customer Service Bot**
- Order lookup, FAQ, ticket creation, sentiment analysis, escalation

#### Project Structure Template

```python
# capstone.py
"""
[PROJECT NAME]
Author: [Your name]
Date: [Date]

Key features:
- [Feature 1]
- [Feature 2]
- [Feature 3]

Skills demonstrated:
- Python OOP, data structures, file I/O
- Claude API with tool use
- Multi-turn conversations with persistent memory
- Error handling and production patterns
"""

def main():
    print("Welcome to [Your Project Name]")
    # your code here

if __name__ == "__main__":
    main()
```

#### GitHub Portfolio Setup

```bash
git init
git add .
git commit -m "Initial commit: AI agent portfolio"
git branch -M main
git remote add origin https://github.com/yourusername/ai-portfolio
git push -u origin main
```

---

## Daily Progress Tracker

| Day | Topic | Build | Status |
|-----|-------|-------|--------|
| 1 | Variables, Logic, Functions | Study Tracker CLI | [ ] |
| 2 | Lists, Dicts, Data Structures | Conversation Memory | [ ] |
| 3 | OOP, File I/O, JSON | Persistent Agent Memory | [ ] |
| 4 | Modules, Env, Advanced Python | Project Scaffolding | [ ] |
| 5 | Claude API, Streaming | AI Tutor CLI | [ ] |
| 6 | Tool Use, Agentic Loop | Research Agent | [ ] |
| 7 | Prompt Engineering | Prompt Workbench | [ ] |
| 8 | Multi-Agent Systems | Support Bot System | [ ] |
| 9 | Production Patterns | Complete Pipeline | [ ] |
| 10 | Capstone + Career Launch | Portfolio Project | [ ] |

---

## Month 2-3 Roadmap

**Month 2 — Intermediate:**
- LangChain and LlamaIndex frameworks
- Vector databases (Pinecone, ChromaDB) for RAG
- Fine-tuning concepts
- Full-stack AI app (FastAPI backend)
- Evaluation frameworks (RAGAS, LangSmith)

**Month 3 — Advanced:**
- Multi-modal AI (vision, audio)
- AI agent deployment (Docker, cloud)
- Building and monetizing AI products
- Contributing to open-source AI tools
- Interview preparation for AI roles

---

## Career, Life, and Business Coaching

### Career Coach

| Role | Salary Range | Key Skills |
|------|-------------|------------|
| AI/ML Engineer | $130K-$200K | Python, APIs, model fine-tuning |
| Prompt Engineer | $90K-$160K | LLM APIs, evaluation, prompt design |
| AI Product Manager | $120K-$180K | AI fundamentals + PM experience |
| LLM App Developer | $100K-$170K | LangChain, RAG, agent development |

**90-day credibility stack:**
1. GitHub with 5+ AI projects
2. One technical blog post per week
3. Build in public on LinkedIn or X
4. Contribute one fix to an AI open-source project

### Life Coach — Consistency System

- **Habit Stacking** (Clear, 2018): Attach coding to an existing habit
- **Implementation Intentions** (Gollwitzer, 1999): Specify when, where, and what
- **The 2-Day Rule**: Never miss more than 2 consecutive days
- **Weekly Review**: What did I build? What was hard? What's next?

### Business Coach — Monetization Paths

| Timeline | Path | Revenue Potential |
|----------|------|------------------|
| 1-3 months | Freelance automation scripts | $50-200/hr |
| 3-6 months | Niche AI wrapper apps | $500-2K MRR |
| 6-12 months | AI agency (3-5 clients) | $6K-25K/month |

**The Build-In-Public Flywheel:** Build → Document → Share → Attract → Build Better

---

## Resources

| Category | Resource | URL |
|----------|----------|-----|
| Python | Official Tutorial | https://docs.python.org/3/tutorial/ |
| Python | Automate the Boring Stuff (free) | https://automatetheboringstuff.com |
| AI Dev | Anthropic API Docs | https://docs.anthropic.com |
| AI Dev | Anthropic Cookbook | https://github.com/anthropics/anthropic-cookbook |
| AI Dev | DeepLearning.AI Short Courses | https://www.deeplearning.ai/short-courses/ |
| Research | Attention Is All You Need | https://arxiv.org/abs/1706.03762 |
| Research | ReAct (agent reasoning) | https://arxiv.org/abs/2210.03629 |
| Research | Chain of Thought | https://arxiv.org/abs/2201.11903 |

---

> **One principle to carry forward:** The developers who succeed in AI are not those who know the most theory — they are those who ship the most working things. Every day, build something. It doesn't have to be perfect. It has to be real.
