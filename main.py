import tkinter as tk
from tkinter import ttk


def send_message():
    message = entry.get()
    if message:
        chat_box.configure(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: ", "you")
        chat_box.insert(tk.END, message + "\n")
        chat_box.configure(state=tk.DISABLED)
        entry.delete(0, tk.END)
    send_bot_answer(message)


def send_bot_answer(prompt: str):
    bot_answer = get_bot_answer(prompt)
    chat_box.configure(state=tk.NORMAL)
    chat_box.insert(tk.END, "Bot: ", "bot")
    chat_box.insert(tk.END, bot_answer + "\n")
    chat_box.configure(state=tk.DISABLED)


def get_bot_answer(prompt: str) -> str:
    return "pede"


def clear_chat():
    chat_box.configure(state=tk.NORMAL)
    chat_box.delete('1.0', tk.END)
    chat_box.configure(state=tk.DISABLED)


# Create the main window
window = tk.Tk()
window.title("ChatBot3000")

# Configure window style
style = ttk.Style()
style.configure("TFrame", background="#ececec")
style.configure("TButton", background="#b3b3b3")
style.configure("TLabel", background="#ececec")
style.configure("TEntry", background="#ffffff")

# Create a frame for the chat display
chat_frame = ttk.Frame(window)
chat_frame.pack(padx=10, pady=10)

# Create the chat display
chat_box = tk.Text(chat_frame, state=tk.DISABLED, width=50, height=20, bg="#ffffff")
chat_box.pack()
chat_box.tag_config("you", foreground="red")
chat_box.tag_config("bot", foreground="blue")

# Create a frame for the message entry field and buttons
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x")

# Create the message entry field
entry = ttk.Entry(input_frame, width=40)
entry.pack(side="left", fill="x", expand=True)

# Create the send button
send_button = ttk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side="left", padx=5)

# Create the clear button
clear_button = ttk.Button(input_frame, text="Clear", command=clear_chat)
clear_button.pack(side="left", padx=5)

# Run the main event loop
window.mainloop()
