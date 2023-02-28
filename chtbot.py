import re
import random
import tkinter as tk

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except:
        return None

def chat():
    def on_send():
        nonlocal chat_history
        nonlocal entry_box
        nonlocal response_label

        user_input = entry_box.get().lower()
        entry_box.delete(0, tk.END)

        if user_input in ['exit', 'quit', 'bye', 'goodbye']:
            chat_history += "Bot: Goodbye!\n"
            response_label.config(text=chat_history)
            entry_box.config(state=tk.DISABLED)

        # Check if input is a mathematical expression
        elif re.match('^\d+(\.\d+)?([\+\-\*\/]\d+(\.\d+)?)+$', user_input):
            result = evaluate_expression(user_input)
            if result is not None:
                chat_history += f"You: {user_input}\nBot: The result is {result}.\n"
            else:
                chat_history += "Bot: Sorry, I could not evaluate the expression.\n"

            response_label.config(text=chat_history)

        # Check if input is a question about the chatbot's capabilities
        elif 'what can you do' in user_input:
            chat_history += "Bot: I'm a calculator chatbot. I can evaluate mathematical expressions like '2+2'.\n"
            response_label.config(text=chat_history)

        # Handle unknown inputs
        else:
            responses = ["Bot: I'm sorry, I don't understand.",
                         "Bot: Can you rephrase that?",
                         "Bot: I'm not sure what you mean.",
                         "Bot: Could you clarify?",
                         "Bot: I didn't get that, can you try again?"]
            chat_history += random.choice(responses) + "\n"
            response_label.config(text=chat_history)

    # Create the chatbot UI
    window = tk.Tk()
    window.title("Calculator Chatbot")

    chat_history = "Bot: Hi! I'm a calculator chatbot. What's your name?\n"
    response_label = tk.Label(window, text=chat_history, font=("Arial", 12))
    response_label.pack(padx=10, pady=10)

    entry_box = tk.Entry(window, font=("Arial", 12))
    entry_box.pack(side=tk.LEFT, padx=10, pady=10)

    send_button = tk.Button(window, text="Send", font=("Arial", 12), command=on_send)
    send_button.pack(side=tk.LEFT, padx=10, pady=10)

    entry_box.focus_set()
    window.mainloop()

if __name__ == '__main__':
    chat()

