"""A friendly rule-based chatbot with memory and a saved conversation log."""

from datetime import datetime
from pathlib import Path
import re


LOG_FILE = Path(__file__).with_name("chat_history.txt")


def clean_message(message):
    """Normalize text so matching works with capitals and punctuation."""
    return re.sub(r"[^a-z0-9\s]", "", message.lower()).strip()


def get_name(message):
    """Extract a name from an introduction such as 'my name is Alex'."""
    match = re.search(r"(?:my name is|call me)\s+([a-z]+)", clean_message(message))
    return match.group(1).title() if match else None


def get_reply(message, user_name):
    """Return a reply, whether to exit, and the current remembered name."""
    cleaned = clean_message(message)
    name = get_name(message)

    if name:
        return f"Nice to meet you, {name}! I'll remember your name during this chat.", False, name
    if cleaned in {"bye", "goodbye", "exit", "quit", "stop"}:
        farewell = f"Goodbye, {user_name}!" if user_name else "Goodbye!"
        return "It was nice chatting with you. " + farewell, True, user_name
    if any(word in cleaned.split() for word in {"hello", "hi", "hey", "greetings"}):
        greeting = f"Hello, {user_name}!" if user_name else "Hello!"
        return greeting + " How can I help you today?", False, user_name
    if "how are you" in cleaned or "hows it going" in cleaned:
        return "I'm doing great, thanks for asking! How are you?", False, user_name
    if cleaned in {"good", "great", "fine", "awesome", "im good", "im fine"}:
        return "Glad to hear that! What would you like to talk about?", False, user_name
    if "your name" in cleaned or "who are you" in cleaned:
        return "I'm Nova, a rule-based Python chatbot created for this project.", False, user_name
    if "my name" in cleaned or "what is my name" in cleaned:
        if user_name:
            return f"Your name is {user_name}.", False, user_name
        return "I don't know your name yet. Try: 'My name is Alex'.", False, user_name
    if "time" in cleaned:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}.", False, user_name
    if "date" in cleaned or "day" in cleaned:
        return f"Today is {datetime.now().strftime('%A, %d %B %Y')}.", False, user_name
    if "help" in cleaned or "what can you do" in cleaned or "options" in cleaned:
        return (
            "I can greet you, remember your name, answer simple questions, tell you the "
            "date or time, and save this chat. Try asking 'Who are you?' or say 'bye' to exit."
        ), False, user_name
    if "thank" in cleaned:
        return "You're welcome!", False, user_name
    if "good morning" in cleaned or "good evening" in cleaned:
        return "Hello! I hope your day is going well.", False, user_name
    if "love" in cleaned or "great job" in cleaned:
        return "Thank you! That means a lot.", False, user_name
    if "joke" in cleaned:
        return "Why do Python programmers wear glasses? Because they can't C!", False, user_name
    if "how old am i" in cleaned or "my age" in cleaned:
        return "I don't know your age yet, but age is just a number!", False, user_name
    return "I'm still learning that topic. Type 'help' to see what I can do.", False, user_name


def save_history(history):
    """Save the completed conversation to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(f"\n--- Chat started: {timestamp} ---\n")
        for speaker, message in history:
            file.write(f"{speaker}: {message}\n")


def main():
    """Run the chatbot until the user ends the conversation."""
    user_name = None
    history = []

    print("=" * 48)
    print("       NOVA - RULE-BASED PYTHON CHATBOT")
    print("=" * 48)
    print("Type 'help' to see what I can do, or 'bye' to exit.\n")

    while True:
        try:
            message = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            message = "bye"
            print("bye")

        if not message:
            print("Nova: Please type a message, or type 'help' for ideas.")
            continue

        reply, should_exit, user_name = get_reply(message, user_name)
        history.extend([("You", message), ("Nova", reply)])
        print(f"Nova: {reply}")

        if should_exit:
            save_history(history)
            print(f"Conversation saved to: {LOG_FILE}")
            break


if __name__ == "__main__":
    main()
