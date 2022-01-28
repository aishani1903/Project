import pyttsx3      #text to speech module
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit as wt
import spotipy
import os
import smtplib
from bs4 import BeautifulSoup
import requests

engine = pyttsx3.init('sapi5')      #Speech Application Programming Interface (allow the use of speech recognition and speech synthesis within Windows applications)
voices = engine.getProperty('voices')
#print(voices[1].id)           #when u run, computer shows that it has 2 voices (1M [0] - David, 1F [1] - Zira)
engine.setProperty('voice', voices[1].id)       #sets voice of your engine

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Welcome, all Data Science students and Yusra ma'am. My name is Rachel! Please tell me how may I help you")
#-------------------------------------------------------------------------------

def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1        #pause_threshold gives time to speak (1sec)
        r.energy_threshold = 300        #minimum audio energy to consider for recording
        audio = r.listen(source)

    try:
        print("Recognizing....")            #recogninzing the audio typed
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
#------------------------------------------------------

#def sendEmail(to, content):
    #server = smtplib.SMTP("smtp.gmail.com", 587)
    #server.ehlo()
    #server.starttls()
    #server.login('---@gmail.com', 'i@3o:')
    #server.sendmail('---@gmail.com', to, content)
    #server.close()


if __name__ == "__main__":
    #speak("Aishani")
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks  based on query
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 1)
            speak("According to wikipedia, ")
            speak(result)

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open youtube and play" in query:
            wt.playonyt(query)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "text" in query:
            if 'dhruvi' in query:
                numb = '+919653234705'
                speak("Whats the message for dhurvi")
                mess = takeCommand()
                print(takeCommand())
                #curr = datetime.localtime()
                #currhr = curr.tm_hour
                #currmin = curr.tm_min
                #currsec = curr.tm_sec
                speak("At what time do you wish to send it?")
                hour = int(input("Hour: "))
                min = int(input("Min: "))
                speak("Your message will be sent")
                wt.sendwhatmsg(numb, mess, hour, min)
                speak("Your message has been sent")

            if 'mum' in query:
                numb = '+919867272421'
                speak("Whats the message for mom")
                mess = takeCommand()
                print(takeCommand())
                hour = datetime.datetime.now().hour
                min = datetime.datetime.now().min
                wt.sendwhatmsg(phone_no=numb, message=mess, time_hour= int(hour), time_min=int(min))


        #elif "Open dev c plus plus" in query:
        #    path = "C://Users//Aishani Anavkar//Desktop//RStudio.lnk"
        #    os.startfile(path)
#----------------------------------------------------------------------

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")          #time in string
            speak(f"The time is {strTime}")

        elif "create a list" in query:
            l1 = []
            speak("What should I add to the list? ")
            a = takeCommand()
            l1.append(a)
            speak("Done")
        elif "read it" in query:
            speak(l1)

        elif 'temperature' in query:
            search = 'temperature in mumbai'
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find('div', class_="BNeawe").text
            speak(f'current {search} is {temp}')

        elif "play music" in query:
            music = "C://Users//Aishani Anavkar//Downloads//Final"
            songs = os.listdir(music)
            os.startfile(os.path.join(music, songs[0]))

        elif "stop" in query:
            break





















#brightness adjust
#volumne adjust
#spotify
#reminder
