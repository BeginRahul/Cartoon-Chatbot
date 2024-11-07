import tkinter as tk
from tkinter import scrolledtext

# Improved chatbot responses with more variety
def get_response(user_input):
    responses = {
        "doraemon": "Doraemon is a robotic cat from the future who helps Nobita with futuristic gadgets.",
        "shizuka": "Shizuka is one of Nobita's best friends. She is intelligent, kind-hearted, and loves taking baths!",
        "nobita": "Nobita is a lazy boy who always gets into trouble but finds a way out with the help of Doraemon's gadgets.",
        "tom": "Tom is a cat who is constantly chasing Jerry, a clever little mouse, in the show Tom and Jerry.",
        "jerry": "Jerry is a clever mouse who always outsmarts Tom in the classic cartoon Tom and Jerry."
    }

    for character, response in responses.items():
        if character in user_input:
            return response

    # If character not recognized
    return "I don't know much about that character yet. Try asking about Doraemon, Shizuka, Nobita, Tom, or Jerry!"

# Function to handle sending messages
def send_message():
    user_input = entry.get().lower()
    if user_input:
        chat_log.insert(tk.END, "You: " + user_input + "\n", "user")
        response = get_response(user_input)
        chat_log.insert(tk.END, "Bot: " + response + "\n\n", "bot")
        entry.delete(0, tk.END)

# Creating the main GUI window
window = tk.Tk()
window.title("Cartoon Talks Chatbot")
window.geometry("500x550")
window.resizable(False, False)
window.config(bg="#f0f8ff")

# Adding a chat log with a scrollable text box
chat_log = scrolledtext.ScrolledText(window, wrap=tk.WORD, state="normal", bg="#ffffff", fg="#000000", font=("Arial", 12), padx=10, pady=10)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Customizing the text tags for the chat log
chat_log.tag_configure("user", foreground="blue", font=("Arial", 12, "bold"))
chat_log.tag_configure("bot", foreground="green", font=("Arial", 12))

# Adding a text entry field for the user input
entry = tk.Entry(window, width=60, font=("Arial", 12), bg="#e0f7fa")
entry.pack(pady=10, padx=10, ipady=5)

# Adding a send button with styling
send_button = tk.Button(window, text="Send", font=("Arial", 10), bg="#00acc1", fg="#ffffff", activebackground="#00838f", command=send_message)
send_button.pack(pady=2)

# Function to bind the Enter key to the send button
window.bind('<Return>', lambda event: send_message())

# Starting the main loop
window.mainloop()
