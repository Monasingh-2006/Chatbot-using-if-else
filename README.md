📝 Project Description

This is a basic rule-based chatbot implemented in Python using simple if-else conditions. The chatbot responds to user inputs by matching predefined keywords or phrases and returns corresponding replies.

This project is great for beginners to understand how chatbots work without complex natural language processing or machine learning.

💡 Features

Responds to greetings like "hello", "hi"

Answers common questions like "how are you?", "what is your name?"

Handles simple conversation flows with conditional logic

Easy to extend by adding more if-else blocks for new responses

🔧 Requirements

Python 3.x installed on your machine

No external libraries required — runs with standard Python.

🚀 How to Run

Download the chatbot.py script.

Open terminal or command prompt.

Run the script with:

python chatbot.py


Type your message and chat with the bot!

📄 Sample Code Snippet
while True:
    user_input = input("You: ").lower()
    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")
    elif user_input == "how are you?":
        print("Bot: I'm fine, thank you!")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
