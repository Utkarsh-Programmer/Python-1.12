import speech_recognition as sr  # voice commands
import webbrowser  # browser based work
import pyttsx3  # let Jarvis speak
import music_library
import requests

# recognize our speech
recognizer = sr.Recognizer()

# initializing pyttsx3
engine = pyttsx3.init()

# news API
news_api = "a53d16f1efca4e8391f16db2cfb61660"


def speak(text):
    """makes jarvis speak."""
    engine.say(text)
    engine.runAndWait()


def process_command(task):
    """performs the given commands."""
    if "open google" in task.lower():
        webbrowser.open("https://www.google.com")
    elif "open chrome" in task.lower():
        webbrowser.open("https://www.chrome.com")
    elif "open facebook" in task.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in task.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in task.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open twitter" in task.lower():
        webbrowser.open("https://www.twitter.com")
    elif "open amazon" in task.lower():
        webbrowser.open("https://www.amazon.in")
    elif "open flipkart" in task.lower():
        webbrowser.open("https://www.flipkart.com")
    elif "open github" in task.lower():
        webbrowser.open("https://www.github.com")
    elif task.lower().startswith("play"):
        song = task.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    elif "news" in task.lower():
        response = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")
        if response.status_code == 200:
            # parse the json response
            data = response.json()

            articles = data.get("articles", [])

            # speak headlines
            for article in articles:
                speak(article["title"])
        else:
            pass


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # LISTENING FOR THE WAKE WORD 'Jarvis'
        # recognize speech using Sphinx
        r = sr.Recognizer()
        print("Recognizing...\n")
        try:
            # obtain audio from the microphone
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=7, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes sir!")

            # LISTENING FOR THE COMMAND
            with sr.Microphone() as source:
                print("Jarvis Activated...")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                process_command(command)

        except Exception as e:
            print(f"Error; {e}")
