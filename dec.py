import tkinter as tk

def decrypt_text(text):
    decrypted_text = ""
    for char in text:
        decrypted_text += chr(ord(char) - 1)
    return decrypted_text

def decrypt_input():
    encrypted_text = input_entry.get()
    decrypted_text = decrypt_text(encrypted_text)
    output_label.config(text=decrypted_text)

window = tk.Tk()
window.title("Decryption Generator")

input_label = tk.Label(window, text="Enter text to decrypt:")
input_label.pack()

input_entry = tk.Entry(window, width=30)
input_entry.pack()

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_input)
decrypt_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
