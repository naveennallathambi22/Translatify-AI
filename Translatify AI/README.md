
# Voice Translator (AI-Enabled)

An AI-powered Python application that records your speech, automatically recognizes and transcribes it, translates the text into your chosen language using Google Translate, and plays back the translated speech using advanced text-to-speech technology (gTTS). This project leverages cloud-based artificial intelligence APIs for speech recognition, translation, and natural-sounding voice synthesis, making it a smart and interactive language tool for everyday use.

## Features
- Speech recognition
- Language translation
- Text-to-speech playback

## Requirements
- Python 3.8+
- Packages: speechrecognition, googletrans==4.0.0-rc1, gtts, playsound

## Usage
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the script:
   ```
   python src/main.py
   ```

## How it works
- The app records your voice, recognizes the text, translates it, and plays the translated audio.

## License
MIT
