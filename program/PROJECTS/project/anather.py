import nltk
from nltk.chat.util import Chat, reflections

# Define sample conversation patterns and responses
conversation = [
    (r'hi|hello', ['Hello!', 'Hi there!', 'How can I help you today?']),
    (r'how are you', ["I'm just a computer program, but I'm doing well. How can I assist you?"]),
    (r'what is your name', ["I'm a chatbot. You can call me ChatGPT!"]),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
]

# Create a chatbot using NLTK's Chat class
chatbot = Chat(conversation, reflections)

# Start the conversation loop
print("ChatGPT: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("ChatGPT:", response)
