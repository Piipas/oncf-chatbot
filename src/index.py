from init import chatbot
from chatterbot.conversation import Statement
import tkinter as tk


def get_response(user_input):
    response = chatbot.get_response(user_input)
    if float(response.confidence) < 0.50:
        response = Statement(
            text="Désolé, je ne comprends pas cette question.")
    return str(response)


def send_message(event=None):
    user_input = user_entry.get()
    if user_input:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, f"Vous: {user_input}\n")
        user_entry.delete(0, tk.END)
        response = get_response(user_input)
        chat_log.insert(tk.END, f"Bot: {response}\n")
        chat_log.config(state=tk.DISABLED)
        chat_log.yview(tk.END)


root = tk.Tk()
root.title("Intern Guide Bot")

chat_log = tk.Text(root, bd=1, bg="white", height=20,
                   width=50, font=("Arial", 12), state=tk.DISABLED)
chat_log.pack(padx=10, pady=10)

user_entry = tk.Entry(root, bd=1, bg="white", width=50, font=("Arial", 12))
user_entry.pack(padx=10, pady=10)
user_entry.bind("<Return>", send_message)

send_button = tk.Button(root, text="Envoyer", width=12, command=send_message)
send_button.pack(pady=10)

root.mainloop()
