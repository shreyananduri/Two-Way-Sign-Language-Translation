# import cv2
# import imageio.v2 as imageio
# import matplotlib.pyplot as plt
# import tkinter as tk
# from tkinter import simpledialog

# def display_image(image_path, title="Original"):
#     img = imageio.imread(image_path)
#     plt.imshow(img, cmap='gray')
#     plt.title(title)
#     plt.axis('off')
#     plt.show()

# def main():
#     path = 'Reverse Images//'  # Directory containing the images

#     # Create a Tkinter root window
#     root = tk.Tk()
#     root.withdraw()  # Hide the root window

#     # Prompt the user for input using a dialog box
#     user_input = simpledialog.askstring("Input", "Enter a word (without spaces):").upper()

#     if user_input is not None:  # Check if the user clicked "Cancel" or closed the dialog
#         try:
#             # Load and display the image corresponding to the user input
#             image_path = path + user_input + '.png'
#             display_image(image_path, user_input)
#         except FileNotFoundError:
#             print("Image not found for input:", user_input)

# if __name__ == "__main__":
#     main()

import tkinter as tk
from tkinter import simpledialog
import cv2
from pytube import YouTube

# Dictionary mapping words to YouTube video URLs
word_to_url = {
    "THANK YOU": "https://www.youtube.com/watch?v=W_qFjH-GKzA",
    "SORRY": "https://www.youtube.com/watch?v=v7LOMsrEiVI",
    "SNAKE": "https://www.youtube.com/watch?v=AdV7Zn6p0yg",
    "FLY": "https://www.youtube.com/watch?v=kvm9DLxYlGo",
    "PLANE": "https://www.youtube.com/watch?v=_-U30DSj-t0",
    "MAN": "https://www.youtube.com/watch?v=rYTt2LuzVhw",
    "WOMAN": "https://www.youtube.com/watch?v=GoDqsUZU5yk",
    "RAIN": "https://www.youtube.com/watch?v=Xg89XzbXfxc",
    "HELP": "https://www.youtube.com/watch?v=d9fEfBJmy0Y",
    "AGE": "https://www.youtube.com/watch?v=98wq5RZYq90",
    "WATER": "https://www.youtube.com/watch?v=5FSC6Og1RBQ",
    "BIG": "https://youtu.be/a2YWHdD5gKk",
    "CINEMA": "https://youtu.be/VBx8a9gFcQI",
    "COFFEE": "https://youtu.be/JmsjCb19HB4",
    "NUT": "https://youtu.be/QhhIAUupAeo",
    "WRITE": "https://youtu.be/Qt7PxYKRi7c",
    "THIGH": "https://youtu.be/AwFPrmwb9B8",
    "BUTTERFLY": "https://youtu.be/iEN8nrcP1y8",
    "CRICKET": "https://youtu.be/G-zchviTHUI"
}

def play_youtube_video(video_url, word):
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    video_capture = cv2.VideoCapture(stream.url)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Add the word on top of the video frame with classic font and black color
        cv2.putText(frame, word, (50, 40), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 2)

        cv2.imshow("YouTube Video", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def main():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user for input using a dialog box
    user_input = simpledialog.askstring("Input", "Enter a word (without spaces):").upper()

    if user_input in word_to_url:  # Check if the word is in the dictionary
        # Play the corresponding YouTube video with the word displayed on top
        play_youtube_video(word_to_url[user_input], user_input)
    else:
        # Display an error message if the word is not found in the dictionary
        print("Error: Video not found for input:", user_input)

if __name__ == "__main__":
    main()
