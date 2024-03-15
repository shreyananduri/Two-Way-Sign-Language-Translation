import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

def predict_sign():
    # Execute the "app.py" script
    subprocess.Popen(["python", "app.py"])

def convert_to_text():
    # Execute the "reverse_recognition.py" script
    subprocess.Popen(["python", "reverse_recognition.py"])

def exit_program():
    # Exit the program
    root.destroy()

# Create the main Tkinter window
root = tk.Tk()
root.title("Talk To The Hand - Indian Sign Language Translator")

# Load and resize the logo
logo_image = Image.open("C:/Users/shrey/OneDrive/Desktop/logoimg.png")  #Replace "logo.png" with the path to your logo image
logo_image = logo_image.resize((93, 93))
logo = ImageTk.PhotoImage(logo_image)

# Create a frame for the header
header_frame = ttk.Frame(root)
header_frame.pack(pady=10)

# Create a label for the logo and app name
logo_label = tk.Label(header_frame, image=logo)
logo_label.pack(side=tk.LEFT, padx=2)
app_name_label = tk.Label(header_frame, text="Talk To The Hand - Indian Sign Language Translator", font=("Helvetica", 16))
app_name_label.pack(side=tk.LEFT)

# Create a frame to hold the buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=30)

# Create buttons for each action with some styling
btn_predict_sign = ttk.Button(button_frame, text="Predict Sign", command=predict_sign)
btn_predict_sign.pack(side=tk.LEFT, padx=10)

btn_convert_to_text = ttk.Button(button_frame, text="Convert to Text", command=convert_to_text)
btn_convert_to_text.pack(side=tk.LEFT, padx=10)

btn_exit = ttk.Button(button_frame, text="Exit", command=exit_program)
btn_exit.pack(side=tk.LEFT, padx=10)

root.geometry("600x400")  # Set window size

# Run the Tkinter event loop
root.mainloop()
