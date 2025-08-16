# Simple chatbot using if-else

print("Hello! I'm ChatBot. Ask me something.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello there!")
    elif user_input == "how are you":
        print("Bot: I'm just a program, but I'm doing fine!")
    elif user_input == "what is your name":
        print("Bot: I'm a simple chatbot.")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
