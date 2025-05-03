# Mini_Voice_Controlled_Web_Search_Assistant
A simple Python voice assistant that uses speech recognition and text-to-speech to let users search for products on **Amazon** or **Temu** by speaking commands like `amazon` or `temu,` followed by the search term.

## 📦 Technologies Used

- `SpeechRecognition` — For converting speech to text.
- `pyttsx3` — For offline text-to-speech.
- `webbrowser` — To open URLs in the default browser.

## 📜 Installation

First, make sure you have Python 3 installed. Then, install the required dependencies:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

**Note:**  
`SpeechRecognition` requires `PyAudio`. If you encounter issues installing `PyAudio`, you can install it using:

```bash
pip install pipwin
pipwin install pyaudio
```

## 🚀 How to Use

1. Run the script:

```bash
python voice_search.py
```

2. The assistant will listen for your command. Say for example:
- `amazon` → it will ask what you want to search for on Amazon.
- `temu` → it will ask what you want to search for on Temu.

3. After you respond, your browser will open with the search results.

## 🎯 Example Flow

```
Adjusting for ambient noise...
Listening...
(User says: "amazon")
Adjusting for ambient noise...
Listening...
(User says: "bluetooth headphones")
👉 It will open: https://www.amazon.com/s?k=bluetooth+headphones
```


