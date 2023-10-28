import tkinter as tk # Import the tkinter module which is the standard GUI (Graphical User Interface) package for Python.

def decrypt_text(text): # Define a function named encrypt_text that takes a string as input and returns an encrypted version of the string.
    decrypted_text = ""
    for char in text: # Iterate through each character in the input string.
        decrypted_text += chr(ord(char) - 1) # Convert each character to its corresponding ASCII value, add 1 to it, and convert it back to the corresponding character.
    return decrypted_text # Return the encrypted string.

def decrypt_input(): # Define a function named encrypt_input that retrieves text from an Entry widget, encrypts it using the encrypt_text function, and displays the result in a Label widget.
    encrypted_text = input_entry.get() # Retrieve the text from the Entry widget.
    decrypted_text = decrypt_text(encrypted_text) # Encrypt the retrieved text using the encrypt_text function.
    output_label.config(text=decrypted_text) # Display the encrypted text in the Label widget.

window = tk.Tk() # Create a main window instance.
window.title("Decryption Generator") # Set the title of the main window.

input_label = tk.Label(window, text="Enter text to decrypt:") # Create a Label widget for displaying a text prompt.
input_label.pack() # Place the Label widget in the main window.

input_entry = tk.Entry(window, width=30) # Create an Entry widget for user input.
input_entry.pack() # Place the Entry widget in the main window.

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_input) # Create a Button widget for triggering the encryption process.
decrypt_button.pack() # Place the Button widget in the main window

output_label = tk.Label(window, text="") # Create a Label widget for displaying the encrypted text.
output_label.pack() # Place the Label widget in the main window.

window.mainloop() # Start the GUI event loop.
