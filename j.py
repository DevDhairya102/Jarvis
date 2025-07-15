import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time

# Initialize JARVIS voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# Set JARVIS voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)  # Reduces background noise
            audio = listener.listen(source, timeout=5, phrase_time_limit=5)
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
            print(f"🗣️ You said: {command}")
            return command
    except sr.WaitTimeoutError:
        print("⏱️ Listening timed out while waiting for phrase.")
    except sr.UnknownValueError:
        print("❌ Could not understand your speech.")
    except sr.RequestError as e:
        print(f"🔌 Could not request results; {e}")
    return ""


def run_jarvis():
    command = take_command()
    print(f"Command: {command}")
    if command == "":
        return  # Skip empty command
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time}')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open google' in command:
        talk("Opening Google")
        pywhatkit.search("Google")
    elif command:
        talk("Sorry, I didn't get that.")

# Run JARVIS in a loop
while True:
    run_jarvis()
    time.sleep(1)
    talk("Do you want me to do something else?")
    user_input = take_command()

    if 'exit' in user_input or 'stop' in user_input:
        talk("Okay, goodbye!")
        break  
