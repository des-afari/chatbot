from responses import responses


def get_response(user_input):
    user_input = user_input.lower()
    
    for key in responses.keys():
        if key in user_input:
            return responses[key]
        
    return "I'm sorry, I don't understand that. Can you please rephrase?"


def chat():
    print("Chatbot: Hi, what can I help you with today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['bye', 'exit', 'quit', 'goodbye', 'see you', 'talk to you later']:
            print("Chatbot: Goodbye! Have a great day.")
            break

        response = get_response(user_input)
        print(f"Chatbot: {response}")

chat()