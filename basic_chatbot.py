# Basic Chatbot - Task 4
# CodeAlpha Python Internship
# simple rule based chatbot that replies based on what user types
# used if-elif conditions to match keywords

def get_reply(message):
    message = message.lower()

    # greetings
    if "hello" in message or "hi" in message or "hey" in message:
        return "Hi there! How can I help you?"

    elif "how are you" in message:
        return "I'm doing good, thanks for asking! How about you?"

    elif "your name" in message or "who are you" in message:
        return "I'm CodeBot, a simple chatbot made with Python!"

    elif "help" in message or "what can you do" in message:
        return "I can chat with you! Try saying hello, ask how I am, or ask for a joke :)"

    elif "joke" in message or "funny" in message:
        return "Why do programmers prefer dark mode? Because light attracts bugs! haha"

    elif "python" in message:
        return "Python is a great programming language! I was made using Python :)"

    elif "age" in message or "how old" in message:
        return "I was just created so I'm pretty young haha"

    elif "thank" in message or "thanks" in message:
        return "You're welcome! Let me know if you need anything else."

    elif "time" in message:
        return "Sorry I don't have access to real time data. Check your phone for the time!"

    elif "weather" in message:
        return "I can't check weather right now. Try Google for that!"

    elif "bye" in message or "goodbye" in message or "exit" in message:
        return "Goodbye! Have a great day!"

    else:
        return "Hmm I didn't understand that. Can you try asking something else?"


# main loop
print("=== CodeBot - Simple Chatbot ===")
print("Type 'bye' to exit\n")

while True:
    user_input = input("You: ")

    if user_input.strip() == "":
        print("Bot: Please type something!")
        continue

    reply = get_reply(user_input)
    print("Bot: " + reply)
    print()

    # stop if user says bye
    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break
