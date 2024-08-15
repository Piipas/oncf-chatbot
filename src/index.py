from init import chatbot
from chatterbot.conversation import Statement
import tkinter as tk
import customtkinter as ctk
from tkinter import RIGHT, LEFT


# def get_response(user_input):
#     response = chatbot.get_response(user_input)
#     print(response.confidence)
#     if float(response.confidence) < 0.40:
#         response = Statement(text="Désolé, je ne comprends pas cette question.")
#     return str(response)


# def send_message(event=None):
#     user_input = user_entry.get().lower()
#     if user_input:
#         chat_log.config(state=tk.NORMAL)
#         chat_log.insert(tk.END, f"Vous: {user_input}\n")
#         user_entry.delete(0, tk.END)
#         response = get_response(user_input).replace("[newline]", "\n")
#         chat_log.insert(tk.END, f"Bot: {response}\n")
#         chat_log.config(state=tk.DISABLED)
#         chat_log.yview(tk.END)


class ONCFChatBot(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ONCF Assistant")
        self.geometry("620x600")
        self._set_appearance_mode("light")

        self.background_color = "#EBEBEB"
        self.user_bubble_background = "#31D190"
        self.bot_bubble_text = "#000000"
        self.bot_bubble_background = "#F2F2F2"
        self.user_bubble_text = "#FFFFFF"

        # Create main frames
        # self.sidebar_frame = ctk.CTkFrame(self, width=200, height=600)
        # self.sidebar_frame.grid(row=0, column=0, sticky="ns", padx=10)

        self.dynamic_frame = ctk.CTkFrame(self, fg_color="#EBEBEB")
        self.dynamic_frame.grid(row=0, column=0, sticky="ns")

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create widgets in the sidebar
        # self.create_sidebar_widgets()
        self.show_chat()

    def create_sidebar_widgets(self):
        self.label = ctk.CTkLabel(self.sidebar_frame, text="Menu", font=("Arial", 24))
        self.label.pack(pady=20)

        self.add_student_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Profile",
        )
        self.add_student_button.pack(pady=5, fill="x")

        self.add_student_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Parametres",
        )
        self.add_student_button.pack(pady=5, fill="x")

        self.view_students_button = ctk.CTkButton(
            self.sidebar_frame, text="Nouvelle discussion"
        )
        self.view_students_button.pack(pady=5, fill="x")

    def show_chat(self):
        self.clear_dynamic_frame()

        self.canvas = tk.Canvas(
            self.dynamic_frame,
            bg=self.background_color,
            height=530,
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        scrollbar = ctk.CTkScrollbar(
            self.dynamic_frame,
            orientation="vertical",
            command=self.canvas.yview,
        )
        self.scrollable_frame = ctk.CTkFrame(self.canvas, fg_color="transparent")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw", width=600
        )
        self.canvas.configure(yscrollcommand=scrollbar.set, width=600)

        self.canvas.grid(row=0, column=0, sticky="ns")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.user_input = ctk.CTkEntry(
            self.dynamic_frame,
            height=40,
            placeholder_text="Votre message ici...",
            font=("Arial", 15),
            corner_radius=40,
        )
        self.user_input.grid(row=1, column=0, padx=10, pady=10, sticky="we")
        self.user_input.bind("<Return>", self.send_message)
        self.user_input.focus()

    def insert_message(self, sender, message, tag):
        bubble_frame = ctk.CTkFrame(
            self.scrollable_frame,
            corner_radius=10,
            fg_color=(
                self.user_bubble_background
                if tag == "user"
                else self.bot_bubble_background
            ),
        )

        # Styling based on sender
        if tag == "user":
            bubble_frame.configure()
            bubble = ctk.CTkLabel(
                bubble_frame,
                text=message,
                justify="left",
                wraplength=500,
                text_color=self.user_bubble_text,
            )
            bubble.pack(padx=10, pady=10, side=RIGHT, expand=True)
        else:
            bubble_frame.configure()
            bubble = ctk.CTkLabel(
                bubble_frame,
                text=message,
                justify="left",
                wraplength=500,
                text_color=self.bot_bubble_text,
            )
            bubble.pack(padx=10, pady=10, side=LEFT, expand=True)

        bubble_frame.pack(
            pady=5,
            padx=(50, 20) if tag == "user" else (20, 50),
            anchor="e" if tag == "user" else "w",
        )

        # Scroll to the bottom
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def get_response(self, prompt):
        response = chatbot.get_response(prompt)
        print(response.confidence)
        if float(response.confidence) < 0.40:
            response = Statement(text="Désolé, je ne comprends pas cette question.")
        return str(response)

    def send_message(self, event: None):
        prompt = self.user_input.get().lower()

        if prompt:
            self.insert_message("", prompt, "user")
            self.user_input.delete(0, tk.END)

            response = self.get_response(prompt).replace("[newline]", "\n")
            self.insert_message("", response, "bot")

    def clear_dynamic_frame(self):
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


# root = tk.Tk()
# root.title("ONCF")
# root.geometry("1000x600")

# chat_log = tk.Text(
#     root, bd=1, bg="white", height=20, width=50, font=("Arial", 12), state=tk.DISABLED
# )
# chat_log.pack(padx=10, pady=10)

# user_entry = tk.Entry(root, bd=1, bg="white", width=50, font=("Arial", 12))
# user_entry.pack(padx=10, pady=10)
# user_entry.bind("<Return>", send_message)

# send_button = tk.Button(root, text="Envoyer", width=12, command=send_message)
# send_button.pack(pady=10)

# root.mainloop()

if __name__ == "__main__":
    app = ONCFChatBot()
    app.mainloop()
