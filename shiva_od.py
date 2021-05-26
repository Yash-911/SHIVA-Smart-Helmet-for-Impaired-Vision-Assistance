import os

import datetime
import speech_recognition as sr
import pyaudio 
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyjokes
import pyttsx3
import psutil               

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tell_time():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is")
    speak(Time)

def tell_date():
    Day = datetime.datetime.now().strftime("%A")
    Date = datetime.datetime.now().strftime("%d %B %Y")
    speak("Today is")
    speak(Day)
    speak(Date)

def wish():
    speak("Welcome back Sir!")
    Hour = datetime.datetime.now().hour
    if Hour >= 6 and Hour < 12:
        speak("Good Morning!")
    elif Hour >= 12 and Hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("SHIVA at your service! How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold=1
        #audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        speak("Failed to Recognize. Please try again.")
        return "None"

    return query

def wiki(query):
    print("Searching...")
    speak("Searching...")
    query = query.replace("wikipedia", " ")
    result = wikipedia.summary(query, sentences=2)
    print()
    print(result)
    speak(result)

def sendEmail():
    try:
        speak("What should I say?")
        content = takeCommand()

        emails={'Yash':'pyash6291@gmail.com','Rutvik':'rutviksanghvi21@gmail.com','Aakash':'aakashshetty1999@gmail.com','Siddhesh':'siddheshsave99@gmail.com'}
        while content == "None":
            content=take_command()
        speak('Whom should I send?')
        listen=take_command()
        while listen == "None":
            listen=take_command()
        if listen == "Yash":
            to=emails.get("Yash")
        elif listen == "Rutvik":
            to=emails.get("Rutvik")
        elif listen == "Siddhesh":
            to=emails.get("Siddhesh")
        elif listen == "Aakash" or listen == "Akash":
            to=emails.get("Aakash")

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('teamshiva.ai@gmail.com','shiva12345')
        server.sendmail('teamshiva.ai@gmail.com', to, content)
        server.close()
        speak("Email sent successfully!")
    except Exception as e:
        speak("Unable to send Email!")
    
def digital_assistant():    
    speak("Where do you want to navigate to?")
    data = take_command()
    listening = True
    location_url = "https://www.google.com/maps/place/" + str(data)
    speak("Hold on Sir, I will show you where " + data + " is.")
    maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
    os.system(maps_arg)

    if "stop listening" in data:
        listening = False
        print('Listening stopped')
        return listening

def chrome():
    speak("What should I search?")
    search = takeCommand().lower()
    driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
    driver.implicitly_wait(1)
    driver.maximize_window()
    driver.get("https://www.google.com/search?q=" + str(search))


def playSongs():
    songs_dir = 'D:\Songs'
    print("Songs Played")
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[525]))

def remember():
    speak('What should I remember?')
    data = takeCommand()
    speak("You asked to remember that " + data)
    rem = open('data.txt', 'w')
    rem.write(data)
    rem.close()

def recall():
    rem = open('data.txt', 'r')
    if os.stat('data.txt').st_size == 0:
        speak("You didn't ask me to remember anything.")
    else:
        speak("You asked me to remember that " + rem.read())
        
def screenshot():
    img = pyautogui.screenshot()
    img.save("ss_saver/ss.png")
    speak("Screenshot taken.")

def cpuUsage():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage + "%")
    battery = psutil.sensors_battery()
    speak("Battery is at " + str(battery.percent) + "%")

def joke():
    jokes = pyjokes.get_joke()
    print(jokes)
    speak(jokes)

if __name__ == '__main__':
    wish()
    wake = "shiva"
    while True:
        que = takeCommand().lower()
        if que.count(wake) > 0:
            speak("Ready")
            query = takeCommand().lower()
            if 'time' in query:
                tell_time()
            
            elif 'date' in query:
                tell_date()
            
            elif 'wikipedia' in query:
                wiki(query)
            
            elif 'email' in query:
                sendEmail()
            
            elif 'navigation' in query:
                digital_assistant(data)

            elif 'chrome' in query:
                chrome()
            
            elif 'logout' in query:
                os.system("shutdown -l")
            
            elif 'shutdown' in query:
                os.system("shutdown /s /t 1")
            
            elif 'restart' in query:
                os.system("shutdown /r /t 1")
            
            elif 'song' in query:
                playSongs()

            elif 'remember this' in query:
                remember()

            elif 'remember anything' in query:
                recall()
            
            elif 'screenshot' in query:
                screenshot()

            elif 'usage' in query:
                cpuUsage()

            elif 'joke' in query:
                joke()

            elif "detection" in query:
                os.system('python object_detection.py')

            elif 'character' in query:
                print("Starting OCR.........")
                os.system('python ocr2.py --east frozen_east_text_detection.pb')

        elif 'offline' in que:
            print("See you soon...")
            speak("See you soon...")
            quit()
        
        elif 'bye' in que:
            print("See you soon...")
            speak("See you soon...")
            quit()