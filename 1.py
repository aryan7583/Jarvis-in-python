import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good Afternoon A J!")

    else:
        speak("good evening!")
    
    speak("i am  jarvis. please tell me how may i help you aaryan sir")


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please..")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
    
        query = takeCommand().lower()
     # Logic for executing tasks based on query

        if 'wikipedia' in query:

            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube'in query:
            webbrowser.open("youtube.com")

        elif 'open google'in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow'in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Aryan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to aryan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aryanjadhav172001Email@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend aryan bhai. I am not able to send this email")    







