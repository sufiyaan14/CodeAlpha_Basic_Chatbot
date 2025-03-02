import nltk
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by GitHub Copilot. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright, great!",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. Bye :)"]
    ],
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
def chatbot_conversation():
    print("Hi, I'm a chatbot created by Sufiyaan Hussain. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Bye, take care. See you soon :)")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot_conversation()