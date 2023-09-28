## About the Project

This open-source program is designed to harness the power of AI for real-time text recognition and speech synthesis. It enables instant conversion of text present within the camera's view into digital text, which is then transformed into audible speech using a Text-To-Speech (TTS) library.

## Libraries Utilized

This project leverages the following libraries to achieve its functionality:

-   **OpenCV**: An open-source computer vision library that facilitates image capture and processing.
    
-   **Tesseract**: A powerful Optical Character Recognition (OCR) engine used to extract text from images.
    
-   **gTTS (Google Text-to-Speech)**: A Python library and CLI tool that interfaces with Google Translate's text-to-speech API to convert text into spoken language.
    
-   **VLC**: A versatile multimedia player library that plays the generated speech as an mp3 audio file.
    

## How It Works

The program follows these steps to convert text from the camera feed into audible speech:

1.  **Image Capture**: The program captures an image from the camera feed in real-time.
    
2.  **Text Extraction**: The captured image is sent to Tesseract, which analyzes the image and extracts any text it detects.
    
3.  **Text-To-Speech Conversion (gTTS)**: The extracted text is then passed to the gTTS library, which converts it into speech. This results in an mp3 audio file.
    
4.  **Audio Playback (VLC)**: Finally, the generated mp3 audio file is played back using the VLC library, allowing the user to hear the converted text.

## Getting Started

To use this program, follow these steps:

1.  Clone the repository to your local machine.
    
2.  Install the required libraries listed in the project's requirements file.
    
3.  Run the program, ensuring that your camera is accessible and properly configured.
    
4.  Point the camera at the text you want to recognize, and the program will provide spoken output in real-time.

## Contributions

Contributions to this project are welcome! Whether you want to add features, improve documentation, or fix bugs, feel free to create a pull request and join our community of contributors.

## Acknowledgments

We would like to acknowledge the contributions of the open-source community, without which this project would not have been possible. Thank you to the authors of OpenCV, Tesseract, gTTS, and VLC for their incredible work.
