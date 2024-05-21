from gtts import gTTS
import pygame
import os

def text_to_speech(text):
    # Generate the audio file from the provided text
    tts = gTTS(text, lang='en')  # You can change the language
    filename = '/tmp/speech.mp3'  # Temporary file in temp directory
    tts.save(filename)
    
    # Play the audio file
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():  # Wait until the audio finishes playing
        pygame.time.Clock().tick(10)
    
    os.remove(filename)  # Remove the temporary file after playback

# # Example usage:
# if __name__ == "__main__":
#     text_to_speech("Hello, this is a test of the text to speech conversion.")
