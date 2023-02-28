import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator Chatbot")

        # Create the conversation display
        self.conversation = tk.Text(master, height=20, width=40)
        self.conversation.pack()

        # Create the input box
        self.input_box = tk.Entry(master, width=30)
        self.input_box.pack()

        # Create the send button
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        message = self.input_box.get()
        response = self.get_response(message)

        self.conversation.insert(tk.END, "You: " + message + "\n")
        self.conversation.insert(tk.END, "Bot: " + response + "\n")
        self.input_box.delete(0, tk.END)

    def get_response(self, message):
        try:
            result = eval(message)
            return f"The result of {message} is {result}"
        except:
            return "I'm sorry, I didn't understand that. Please enter a valid math expression."

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
