# Project-VoiceMate
#VoiceMate is a simple yet effective voice assistant that utilizes speech recognition and text-to-speech technologies to interact with users.
import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the TTS engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for a command"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        return ""

def open_youtube():
    """Open YouTube"""
    webbrowser.open("https://www.youtube.com")
    speak("Opening YouTube.")

def search_image(query):
    """Search for an image on Google"""
    url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"
    webbrowser.open(url)
    speak(f"Searching for images of {query}.")

def main():
    """Main function to run the assistant"""
    speak("Hello, how can I help you today?")
    while True:
        command = listen().lower()
        if 'hello' in command:
            speak("Hi there!")
        elif 'how are you' in command:
            speak("I'm just a program, but I'm doing fine. Thank you!")
        elif 'open youtube' in command:
            open_youtube()
        elif 'search for an image of' in command:
            query = command.replace("search for an image of", "").strip()
            search_image(query)
        elif 'exit' in command:
            speak("Goodbye!")
            break
        else:
            speak("I can only respond to a few commands for now.")

if __name__ == "__main__":
    main()

