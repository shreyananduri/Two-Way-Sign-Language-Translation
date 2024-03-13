from gtts import gTTS
# import os

# # Function to convert text to speech
# def text_to_speech(text):
#     # Use the Google Text-to-Speech API to convert text to speech
#     tts = gTTS(text=text, lang='en')
#     # Save the speech as an audio file
#     tts.save('output.mp3')
#     # Play the audio file
#     os.system("start output.mp3")  # This command works on Windows, for other OS, use appropriate command

# # Code for recognizing signs and converting to speech
# # Inside the loop where you detect and recognize signs
# if np.unique(predictions[-10:])[0] == np.argmax(res):
#     if res[np.argmax(res)] > threshold:
#         if len(sentence) > 0:
#             if actions[np.argmax(res)] != sentence[-1]:
#                 sentence.append(actions[np.argmax(res)])
#                 accuracy.append(str(res[np.argmax(res)] * 100))
#         else:
#             sentence.append(actions[np.argmax(res)])
#             accuracy.append(str(res[np.argmax(res)] * 100))

#     if len(sentence) > 1:
#         sentence = sentence[-1:]
#         accuracy = accuracy[-1:]

#     # Convert recognized signs to text
#     recognized_text = ' '.join(sentence)

#     # Convert recognized text to speech
#     text_to_speech(recognized_text)