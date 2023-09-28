import cv2
import pytesseract
from gtts import gTTS
import vlc
import time

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize the VLC media player
instance = vlc.Instance("--no-xlib")
player = instance.media_player_new()

# Create a function to speak text using VLC
def speak(text):
    if text.strip():  # Check if the text is not empty or contains only whitespace
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        media = instance.media_new("output.mp3")
        player.set_media(media)
        player.play()

# Set up the camera
cap = cv2.VideoCapture(2)  # Use the default camera (usually 0)

# Initialize variables
last_detection_time = time.time()  # Set an initial value
detected_text = ""  # Initialize detected_text

while True:
    ret, frame = cap.read()
    
    # Preprocess the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    current_time = time.time()
    
    if current_time - last_detection_time >= 2.0:
        detected_text = pytesseract.image_to_string(thresh)  # Use the preprocessed image
        last_detection_time = current_time
    
    # Display the detected text on the frame
    cv2.putText(frame, detected_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Text Detection", frame)
    
    # Speak the detected text
    speak(detected_text)
    
    # Press 'q' to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
