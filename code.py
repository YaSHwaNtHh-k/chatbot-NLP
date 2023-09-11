import nltk
import random
# Define responses for the chatbot
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a chatbot, but I'm here to help!", "I don't have feelings, but thanks for asking!"],
    "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
}

# Function to generate a response to a user's input
def respond(input_text):
    input_text = input_text.lower() 
    for key in responses:
        if key in input_text:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."

# Main loop for interacting with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = respond(user_input)
    print("Chatbot:", response)