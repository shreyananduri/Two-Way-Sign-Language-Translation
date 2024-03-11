import cv2
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

def display_image(image_path, title="Original"):
    img = imageio.imread(image_path)
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def main():
    path = 'Reverse Images//'  # Directory containing the images

    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user for input using a dialog box
    user_input = simpledialog.askstring("Input", "Enter a word (without spaces):").upper()

    if user_input is not None:  # Check if the user clicked "Cancel" or closed the dialog
        try:
            # Load and display the image corresponding to the user input
            image_path = path + user_input + '.png'
            display_image(image_path, user_input)
        except FileNotFoundError:
            print("Image not found for input:", user_input)

if __name__ == "__main__":
    main()
