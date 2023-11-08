import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack(pady=10)

        self.generated_password = tk.StringVar()
        self.password_entry = ttk.Entry(root, textvariable=self.generated_password)
        self.password_entry.pack()

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.pack(pady=10)

        self.length = tk.IntVar(value=12)
        self.length_spinbox = tk.Spinbox(root, from_=6, to=30, textvariable=self.length)
        self.length_spinbox.pack()

        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special_chars = tk.BooleanVar(value=True)
        self.checkbox_frame = ttk.LabelFrame(root, text="Include:")
        self.checkbox_frame.pack(pady=10)

        tk.Checkbutton(self.checkbox_frame, text="Lowercase", variable=self.include_lowercase).pack()
        tk.Checkbutton(self.checkbox_frame, text="Uppercase", variable=self.include_uppercase).pack()
        tk.Checkbutton(self.checkbox_frame, text="Digits", variable=self.include_digits).pack()
        tk.Checkbutton(self.checkbox_frame, text="Special Characters", variable=self.include_special_chars).pack()

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)


        tk.Checkbutton(self.checkbox_frame, text="Lowercase", variable=self.include_lowercase).pack()
        tk.Checkbutton(self.checkbox_frame, text="Uppercase", variable=self.include_uppercase).pack()
        tk.Checkbutton(self.checkbox_frame, text="Digits", variable=self.include_digits).pack()
        tk.Checkbutton(self.checkbox_frame, text="Special Characters", variable=self.include_special_chars).pack()

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()

    def generate_password(self):
        password_length = self.length.get()
        characters = ""

        if self.include_lowercase.get():
            characters += string.ascii_lowercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_digits.get():
            characters += string.digits
        if self.include_special_chars.get():
            characters += string.punctuation

        if not characters:
            characters = string.ascii_letters + string.digits + string.punctuation

        generated_password = "".join(random.choice(characters) for _ in range(password_length))
        self.generated_password.set(generated_password)

    def copy_to_clipboard(self):
        pyperclip.copy(self.generated_password.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


