import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm fine, thank you!", "I'm doing well!"],
    "what is your name?": ["I'm a chatbot.", "You can call me ChatBot!"],
    "bye": ["Goodbye!", "See you later!"]
}

def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("ChatBot:", random.choice(responses[user_input]))
        elif user_input == "exit":
            print("ChatBot: Goodbye!")
            break
        else:
            print("ChatBot: I don't understand.")

chatbot()

