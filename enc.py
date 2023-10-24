import tkinter as tk

def encrypt_text(text):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + 1) 
    return encrypted_text

def encrypt_input():
    input_text = input_entry.get()
    encrypted_text = encrypt_text(input_text)
    output_label.config(text=encrypted_text)

window = tk.Tk()
window.title("Encryption Generator")

input_label = tk.Label(window, text="Enter text to encrypt:")
input_label.pack()

input_entry = tk.Entry(window, width=30)
input_entry.pack()

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_input)
encrypt_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
