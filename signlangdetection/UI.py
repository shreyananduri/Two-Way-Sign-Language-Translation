import tkinter as tk
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
root.title("Two Way Indian Sign Language Translator")

# Create buttons for each action
btn_predict_sign = tk.Button(root, text="Predict Sign", command=predict_sign)
btn_predict_sign.pack()

btn_convert_to_text = tk.Button(root, text="Convert to Text", command=convert_to_text)
btn_convert_to_text.pack()

btn_exit = tk.Button(root, text="Exit", command=exit_program)
btn_exit.pack()

# Run the Tkinter event loop
root.mainloop()
