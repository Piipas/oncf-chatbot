from init import chatbot

# Create a function to interact with the chatbot
def chat():
    print("Tapez 'exit' pour terminer la conversation.")
    while True:
        try:
            user_input = input("Vous: ")
            if user_input.lower() == 'exit':
                break

            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")

        except (KeyboardInterrupt, EOFError, SystemExit):
            break

if __name__ == '__main__':
    chat()
