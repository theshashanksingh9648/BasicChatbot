# 🤖 Basic Chatbot — CodeAlpha Python Internship Task 4

A simple rule-based chatbot built in Python that responds to user messages using keyword matching and predefined replies.

## 📌 About the Project

This project is part of the **CodeAlpha Python Programming Internship**. The goal was to build a basic conversational chatbot using if-elif logic, functions, and loops — no AI or ML libraries needed!

## 🚀 Features

- Responds to greetings: `hello`, `hi`, `hey`
- Handles common questions like "how are you", "what's your name"
- Tells a programming joke on request
- Talks about Python programming
- Graceful exit when user says `bye` or `exit`
- Handles empty input with a friendly prompt
- Covers 10+ conversation topics

## 🧠 Concepts Used

- `if-elif` conditions
- Functions
- `while` loops
- String methods (`.lower()`, `.strip()`)
- Input/Output

## ▶️ How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/CodeAlpha_BasicChatbot
   cd CodeAlpha_BasicChatbot
   ```
3. Run the script:
   ```bash
   python task4_chatbot.py
   ```

## 💬 Sample Conversation

```
=== CodeBot - Simple Chatbot ===
Type 'bye' to exit

You: hello
Bot: Hi there! How can I help you?

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs! haha

You: thanks
Bot: You're welcome! Let me know if you need anything else.

You: bye
Bot: Goodbye! Have a great day!
```

## 🗨️ Supported Topics

| User Input         | Bot Response                        |
|--------------------|-------------------------------------|
| hello / hi / hey   | Greeting response                   |
| how are you        | Status reply                        |
| your name / who    | Bot introduces itself               |
| help               | Lists what the bot can do           |
| joke / funny       | Tells a programming joke            |
| python             | Talks about Python                  |
| age / how old      | Playful age response                |
| thank / thanks     | Polite acknowledgement              |
| time               | Redirects to phone                  |
| weather            | Redirects to Google                 |
| bye / goodbye      | Farewell and exits                  |

## 📁 Project Structure

```
CodeAlpha_BasicChatbot/
│
├── task4_chatbot.py   # Main chatbot script
└── README.md          # Project documentation
```

## 🏢 Internship

**Organization:** [CodeAlpha](https://www.codealpha.tech)  
**Domain:** Python Programming  
**Task:** Task 4 — Basic Chatbot

---

> Made with ❤️ using Python during the CodeAlpha Internship Program.
