"""
Day 7 Build: Prompt Engineering Workbench

A/B test different prompting strategies on the same task.
Demonstrates: prompt engineering patterns, structured comparison, JSON output.

Usage:
    python prompt_workbench.py

Requirements:
    pip install anthropic python-dotenv
    ANTHROPIC_API_KEY in .env file
"""

import anthropic
import os
import json
import time
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


class PromptExperiment:
    """Compare multiple prompting strategies on the same task."""

    def __init__(self, task_description: str):
        self.task = task_description
        self.results = []

    def run(self, variant_name: str, prompt: str, system: str = None) -> dict:
        start = time.time()

        kwargs = {
            "model": "claude-sonnet-4-6",
            "max_tokens": 512,
            "messages": [{"role": "user", "content": prompt}]
        }
        if system:
            kwargs["system"] = system

        response = client.messages.create(**kwargs)
        elapsed = time.time() - start

        result = {
            "variant": variant_name,
            "response": response.content[0].text,
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "latency_ms": round(elapsed * 1000),
        }
        self.results.append(result)
        print(f"  [{variant_name}] {result['output_tokens']} tokens, {result['latency_ms']}ms")
        return result

    def compare(self) -> None:
        print(f"\n{'='*60}")
        print(f"EXPERIMENT: {self.task}")
        print(f"{'='*60}\n")

        for r in self.results:
            print(f"--- {r['variant']} ---")
            print(f"({r['output_tokens']} tokens, {r['latency_ms']}ms)")
            print(r['response'][:300])
            if len(r['response']) > 300:
                print("  [truncated...]")
            print()

    def save(self, filename: str) -> None:
        with open(filename, "w") as f:
            json.dump({"task": self.task, "results": self.results}, f, indent=2)
        print(f"Results saved to {filename}")


def run_sample_experiment():
    """Run a built-in experiment comparing 4 prompting strategies."""
    exp = PromptExperiment("Explain what a neural network is")

    print(f"Running experiment: '{exp.task}'\n")

    exp.run(
        "Direct",
        "What is a neural network?"
    )

    exp.run(
        "Role-based",
        "What is a neural network?",
        system="You are a university professor teaching AI to first-year students. Use a real-world analogy."
    )

    exp.run(
        "Few-shot",
        """Explain these AI terms using: [term] = [simple analogy] + [technical detail]

Example: Algorithm = Recipe + Step-by-step instructions a computer follows to solve a problem.

Now explain: Neural network =""")

    exp.run(
        "Structured output",
        """Explain 'neural network' using this exact format:
ANALOGY: [a non-technical analogy]
DEFINITION: [1 sentence technical definition]
KEY COMPONENTS: [3 bullet points]
REAL EXAMPLE: [one real-world application]"""
    )

    exp.compare()
    exp.save("prompt_experiment_results.json")


def interactive_mode():
    """Let the user test their own prompts."""
    print("=== Interactive Prompt Tester ===")
    print("Compare two prompts side-by-side.\n")

    task = input("Describe the task (for labeling): ").strip()
    exp = PromptExperiment(task)

    while True:
        variant = input("\nVariant name (or 'done' to compare): ").strip()
        if variant.lower() == "done":
            break

        system = input("System prompt (leave blank for none): ").strip() or None
        print("Enter prompt (type END on a new line when done):")
        lines = []
        while True:
            line = input()
            if line == "END":
                break
            lines.append(line)
        prompt = "\n".join(lines)

        exp.run(variant, prompt, system)

    if exp.results:
        exp.compare()
        save = input("Save results? (y/n): ").strip().lower()
        if save == "y":
            exp.save(f"{task.replace(' ', '_')}_results.json")


def main():
    print("=== Prompt Engineering Workbench ===\n")
    print("1. Run sample experiment (neural network comparison)")
    print("2. Interactive mode (test your own prompts)")
    choice = input("\nChoose (1-2): ").strip()

    if choice == "1":
        run_sample_experiment()
    elif choice == "2":
        interactive_mode()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
