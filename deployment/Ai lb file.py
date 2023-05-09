# Simple Chatbot

# Define the chatbot's name
bot_name = "Chatbot"

# Define a function to greet the user
def greet():
    print("Hello! My name is " + bot_name + ". How can I help you today?")

# Define a function to say goodbye to the user
def goodbye():
    print("Goodbye! Have a nice day.")

# Define a function to handle user input
def handle_input(user_input):
    # Convert the user's input to lowercase
    user_input = user_input.lower()

    # Check if the user is saying hello
    if user_input.startswith('hello') or user_input.startswith('hi'):
        print("Hello! How can I assist you today?")
    # Check if the user is asking for help
    elif user_input.startswith('help'):
        print("I'm here to help! How can I assist you today?")
    # Check if the user is saying goodbye
    elif user_input.startswith('goodbye') or user_input.startswith('bye'):
        goodbye()
        return True
    # Handle any other input
    else:
        print("I'm sorry, I didn't understand what you said. Can you please rephrase your question?")

    return False

# Define the main function to run the chatbot
def run_chatbot():
    greet()

    # Loop to handle user input
    while True:
        user_input = input(">> ")
        if handle_input(user_input):
            break

# Run the chatbot
run_chatbot()
