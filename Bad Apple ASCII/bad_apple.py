import cv2
import numpy as np
import os
import time
import sys
from playsound import playsound
import threading

# Function to convert a grayscale image to ASCII
def image_to_ascii(image, new_width=100, aspect_ratio_correction=2):
    height, width = image.shape
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width / aspect_ratio_correction)
    resized_image = cv2.resize(image, (new_width, new_height))
    
    ascii_chars = "@%#*+=-:. "
    pixels = resized_image / 255.0 * (len(ascii_chars) - 1)
    
    ascii_str = '\n'.join(''.join(ascii_chars[int(pixel)] for pixel in row) for row in pixels)
    
    return ascii_str

# Function to play the video in ASCII at the original speed
def play_video(video_path, audio_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_time = 1 / fps  # Time between frames in seconds
    
    # Start audio playback in a separate thread
    audio_thread = threading.Thread(target=playsound, args=(audio_path,), daemon=True)
    audio_thread.start()
    time.sleep(0.5)
    while cap.isOpened():
        start_time = time.perf_counter()  # Record the frame start time

        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ascii_frame = image_to_ascii(gray_frame)

        sys.stdout.write("\033c")  # Clears the console
        sys.stdout.write(ascii_frame + "\n")
        sys.stdout.flush()

        # Wait until the next frame with higher precision
        while (time.perf_counter() - start_time) < frame_time:
            pass

    cap.release()

video_path = './video.mp4'
audio_path = './audio.mp3'

# Play the ASCII video with audio
play_video(video_path, audio_path)
os.system('cls')
print("The end")
time.sleep(999)
