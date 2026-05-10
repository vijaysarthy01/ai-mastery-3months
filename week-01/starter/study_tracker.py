"""
Day 1 Build: Personal Study Tracker

A CLI app to log study sessions, view progress, and get review recommendations.
Demonstrates: variables, loops, functions, dictionaries, user input.

Usage:
    python study_tracker.py
"""


def add_topic(topics: dict, topic_name: str, hours_studied: float) -> dict:
    topics[topic_name] = topics.get(topic_name, 0) + hours_studied
    print(f"Logged {hours_studied}h for '{topic_name}'. Total: {topics[topic_name]}h")
    return topics


def show_progress(topics: dict) -> None:
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


def recommend_review(topics: dict) -> None:
    """Simple spaced repetition: flag topics with less than 2 hours."""
    print("\n=== Recommended for Review ===")
    needs_review = [(t, h) for t, h in topics.items() if h < 2]
    if not needs_review:
        print("  All topics have enough time logged. Keep it up!")
        return
    for topic, hours in needs_review:
        print(f"  {topic} — needs more time (only {hours}h logged)")


def main():
    topics = {}

    while True:
        print("\n1. Log study session")
        print("2. View progress")
        print("3. Get review recommendations")
        print("4. Quit")

        choice = input("\nChoose (1-4): ").strip()

        if choice == "1":
            topic = input("Topic name: ").strip()
            try:
                hours = float(input("Hours studied: "))
                topics = add_topic(topics, topic, hours)
            except ValueError:
                print("Please enter a valid number for hours.")
        elif choice == "2":
            show_progress(topics)
        elif choice == "3":
            recommend_review(topics)
        elif choice == "4":
            print("Keep learning! Consistency beats intensity.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
