import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "fe137a5e26184325b32e73081896967d"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #Parse the JSON response(r)
            data = r.json()

            #Extract the articles
            articles = data.get('articles', [])

            #Print the headlines
            for article in articles:
                speak(article['title'])

        else:
            #Let openAI handle the request
            pass


if __name__=="__main__":
    speak("Hello")
    while True:
        #Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Listening...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Recognizing...")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            print(f"Recognized: {word}") #See what it actually heard
            recognized_word = word.lower().strip()
            print(f"Recognized: {recognized_word}")
            if "pallavi" in recognized_word:
                speak("Ya")

                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        
        except Exception as e:
            print("Google error; {0}".format(e)) 