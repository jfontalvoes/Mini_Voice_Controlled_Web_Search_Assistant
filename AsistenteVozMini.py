import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()

def speak():
    mic = sr.Microphone()
    with mic as source:
        print("Ajustando al ruido ambiente...")
        recognizer.adjust_for_ambient_noise(source)
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        print("Texto reconocido:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("No se entendió el audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error al conectarse al servicio de reconocimiento: {e}")
        return ""

if "amazon" in speak():
        engine.say("¿Que desea buscar en amazon?")
        engine.runAndWait()
        text = speak()

        if text:
             webbrowser.open(f"https://www.amazon.com/s?k={text}")
        else:
             engine.say("No pude entender lo que dijiste. Intenta nuevamente.")
             engine.runAndWait()

elif "temu" or "temo" in speak():
        engine.say("¿Que desea buscar en Temu?")
        engine.runAndWait()
        text = speak()

        if text:
             webbrowser.open(f"https://www.temu.com/search_result.html?search_key={text}")
        else:
             engine.say("No pude entender lo que dijiste. Intenta nuevamente.")
             engine.runAndWait()