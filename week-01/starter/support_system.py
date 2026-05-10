"""
Day 8 Build: Customer Support Agent System

A multi-tool support chatbot with order lookup, product info, and ticket creation.
Demonstrates: multi-tool agents, agentic loop, simulated databases, multi-turn chat.

Usage:
    python support_system.py

Sample inputs to try:
    "What is the status of order ORD-1001?"
    "Tell me about product PRO-002"
    "I need help, my order is taking too long"

Requirements:
    pip install anthropic python-dotenv
    ANTHROPIC_API_KEY in .env file
"""

import anthropic
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# --- Simulated Databases ---

PRODUCT_DB = {
    "PRO-001": {"name": "AI Starter Kit", "price": 49.99, "stock": 15, "warranty": "1 year"},
    "PRO-002": {"name": "Developer Bundle", "price": 149.99, "stock": 3, "warranty": "2 years"},
    "PRO-003": {"name": "Enterprise Suite", "price": 499.99, "stock": 0, "warranty": "3 years"}
}

ORDER_DB = {
    "ORD-1001": {"product": "PRO-001", "status": "shipped", "tracking": "TRK789"},
    "ORD-1002": {"product": "PRO-002", "status": "processing", "tracking": None},
    "ORD-1003": {"product": "PRO-003", "status": "delivered", "tracking": "TRK456"}
}


# --- Tool Implementations ---

def check_order_status(order_id: str) -> str:
    order = ORDER_DB.get(order_id.upper())
    if order:
        return json.dumps(order)
    return f"Order {order_id} not found."


def check_product_info(product_id: str) -> str:
    product = PRODUCT_DB.get(product_id.upper())
    if product:
        return json.dumps(product)
    return f"Product {product_id} not found."


def create_ticket(issue: str, priority: str, customer_id: str = "unknown") -> str:
    ticket_id = f"TKT-{datetime.now().strftime('%H%M%S')}"
    print(f"\n  [TICKET CREATED] {ticket_id} | Priority: {priority.upper()} | {issue[:60]}")
    return f"Ticket {ticket_id} created successfully. You'll receive an email confirmation."


# --- Tool Schemas ---

TOOLS = [
    {
        "name": "check_order_status",
        "description": "Check the current status and tracking info for a customer order.",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string", "description": "The order ID, e.g. ORD-1001"}
            },
            "required": ["order_id"]
        }
    },
    {
        "name": "check_product_info",
        "description": "Get product details: name, price, stock availability, and warranty.",
        "input_schema": {
            "type": "object",
            "properties": {
                "product_id": {"type": "string", "description": "The product ID, e.g. PRO-001"}
            },
            "required": ["product_id"]
        }
    },
    {
        "name": "create_ticket",
        "description": "Create a support ticket for issues requiring human follow-up.",
        "input_schema": {
            "type": "object",
            "properties": {
                "issue": {"type": "string", "description": "Description of the customer's issue"},
                "priority": {
                    "type": "string",
                    "enum": ["low", "medium", "high", "urgent"],
                    "description": "Priority level"
                },
                "customer_id": {"type": "string", "description": "Customer identifier if known"}
            },
            "required": ["issue", "priority"]
        }
    }
]

TOOL_MAP = {
    "check_order_status": check_order_status,
    "check_product_info": check_product_info,
    "create_ticket": create_ticket
}

SYSTEM_PROMPT = """You are an empathetic, efficient AI customer support agent for TechStore.

Guidelines:
- Acknowledge the customer's concern before diving into solutions
- Use available tools to look up real information — do not guess
- Be concise but thorough
- If you can't fully resolve an issue, create a support ticket
- Escalate to high/urgent priority if the customer expresses significant frustration
- End each response by asking if there's anything else you can help with"""


# --- Agentic Loop ---

def run_turn(history: list, user_input: str) -> str:
    """Process one turn of the conversation, including any tool calls."""
    messages = history + [{"role": "user", "content": user_input}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages
        )

        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
            return ""

        elif response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    func = TOOL_MAP.get(block.name)
                    result = func(**block.input) if func else "Tool not found"
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            messages.append({"role": "user", "content": tool_results})

        else:
            return f"Unexpected stop: {response.stop_reason}"


def main():
    print("\n=== TechStore AI Support ===")
    print("Type 'exit' to end\n")
    print("Agent: Hello! I'm your AI support assistant. How can I help you today?\n")

    history = []

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            print("Agent: Thank you for contacting TechStore support. Have a great day!")
            break

        reply = run_turn(history, user_input)
        print(f"\nAgent: {reply}\n")

        # Update history with the clean text exchange
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
