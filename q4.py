import tkinter as tk
import random
import string

def generate_password():
    password_length = 10  
    characters = string.ascii_letters 
    password = ''.join(random.choice(characters) for i in range(password_length))

    password_label.config(text=f"Generated Password: {password}")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

password_label = tk.Label(root, text="Generated Password: ", font=("Helvetica", 12))
password_label.pack(pady=20)

root.mainloop()