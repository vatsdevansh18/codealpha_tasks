# CodeAlpha Python Internship Tasks

This repository contains the completed tasks for the **CodeAlpha Python Development Internship**.

---

## 📁 Repository Structure

### 🎮 [Task 1: Hangman Game](./Task1/)
A console Hangman game built using Python fundamentals:
- Random word selection across multiple categories
- Visual ASCII hangman stages drawn after each incorrect guess
- Prevents duplicate guesses and tracks win/loss statistics across rounds
- **Key Concepts:** `random`, lists, sets, loops, functions, input validation

### 📈 [Task 2: Stock Portfolio Tracker](./Task2/)
A menu-driven console application to manage and evaluate an investment portfolio:
- Calculates portfolio value, profit/loss, and allocation percentage per stock
- Input validation for ticker symbols and share quantities
- Option to export a timestamped portfolio summary report to a text file
- **Key Concepts:** Dictionaries, arithmetic logic, formatted console tables, file I/O

### ✉️ [Task 3: Email Extraction Automation](./Task3/)
An automation script to parse text files and extract email addresses:
- Uses regular expressions (`re`) to locate email patterns in unstructured text
- Deduplicates email addresses while preserving original order and frequency counts
- Generates and exports a structured report to `extracted_emails.txt`
- **Key Concepts:** Regular expressions (`re`), file handling, data structures, reporting

### 🤖 [Task 4: Basic Rule-Based Chatbot (Nova)](./Task4/)
A rule-based conversational console chatbot named Nova:
- Responds to greetings, common queries, date/time inquiries, jokes, and farewells
- Remembers user context (e.g. user's name) during the session
- Automatically saves chat transcripts to `chat_history.txt`
- **Key Concepts:** Pattern matching, string processing, session state, file handling

---

## 🚀 Getting Started

Ensure you have Python 3.8+ installed.

Clone the repository:
```bash
git clone https://github.com/vatsdevansh18/codealpha_tasks.git
cd codealpha_tasks
```

Navigate to any task directory and run the corresponding script:
```bash
# Example: Running Task 1
cd Task1
python hangman_game.py
```
