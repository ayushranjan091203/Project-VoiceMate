import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
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

# Function to open YouTube
def open_youtube():
    webbrowser.open("https://www.youtube.com")
    speak("Opening YouTube.")

# Function to search for an image on Google
def search_image(query):
    url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"
    webbrowser.open(url)
    speak(f"Searching for images of {query}.")

# Main function to run the assistant
def main():
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

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
