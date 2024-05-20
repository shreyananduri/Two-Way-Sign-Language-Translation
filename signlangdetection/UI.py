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

try:
    # Load and resize the logo
    logo_image = Image.open("logoimg.png")  # Update the file path as needed
    logo_image = logo_image.resize((93, 93))
    logo = ImageTk.PhotoImage(logo_image)
except Exception as e:
    print("Error loading logo image:", e)
    logo = None

# Create a frame for the header
header_frame = ttk.Frame(root)
header_frame.pack(pady=30)

# Create a label for the logo and app name
if logo:
    logo_label = tk.Label(header_frame, image=logo)
    logo_label.grid(row=0, column=0, padx=(10, 0))  

app_name_label = tk.Label(header_frame, text="Talk To The Hand\n\n Indian Sign Language Translator", font=("Helvetica", 16))
app_name_label.grid(row=0, column=1, padx=20)

# Create a frame to hold the buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=50)

# Create buttons for each action with pastel colors
btn_predict_sign = ttk.Button(button_frame, text="Predict Sign", command=predict_sign, style="Pastel.TButton")
btn_predict_sign.grid(row=0, column=0, padx=10)

btn_convert_to_text = ttk.Button(button_frame, text="Convert to Text", command=convert_to_text, style="Pastel.TButton")
btn_convert_to_text.grid(row=0, column=1, padx=10)

btn_exit = ttk.Button(button_frame, text="Exit", command=exit_program, style="Pastel.TButton")
btn_exit.grid(row=0, column=2, padx=10)

# Style for pastel buttons
style = ttk.Style()
style.configure("Pastel.TButton", background="#a8dadc")  # Set the background color to a pastel shade

root.geometry("600x400")  # Set window size

# Run the Tkinter event loop
root.mainloop()