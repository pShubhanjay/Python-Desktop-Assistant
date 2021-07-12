import os
import datetime
import requests, json
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import pyautogui
import psutil

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1)


#change voice
def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    print("Voice changed")
    speak("done sir")


#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M")
    speak("The current time is")
    print(Time)
    speak(Time)


#date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    print(date, month, year)
    speak(date)
    speak(month)
    speak(year)


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning")
        else:
            if (hour >= 12 and hour < 18):
                speak("Good afternoon")
            elif (hour >= 18 and hour < 24):
                speak("Good Evening")
            else:
                speak("Goodnight")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("Good afternoon")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning")
            elif (hour >= 18 and hour < 24):
                speak("Good Evening")
            else:
                speak("Goodnight")
    else:
        speak("night")


#welcome function
def wishme():
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight")

    speak("Please tell me how can i help you?")
    print("How can i help you?")


def wishme_end():
    print("Bye!")
    speak("Bye Bye")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()


#command by user function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #speak(query)
        #print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query


#screenshot function
def screenshot():
    img = pyautogui.screenshot()
    img.save(
        "C:\\Users\\Shubhanjay\\Pictures\\AI SS\\ss.png"
    )


#battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))


#weather condition
def weather():
    api_key = "Your API key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = takeCommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")


def personal():
    print("I am an AI assistant, constantly learning from you")
    speak("I am an AI assistant, constantly learning from you")


if __name__ == "__main__":
    wishme()
    while (True):
        query = takeCommand().lower()

#time

        if ('time' in query):
            time()

#date

        elif ('date' in query):
            date()


#weather
        elif ("weather" in query or "temperature" in query):
            weather()

# changing voice
        elif ("voice" in query):
            speak("for female say female and, for male say male")
            q = takeCommand()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)
        elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)

#searching on wikipedia

        elif ('wikipedia' in query or 'what' in query or 'who' in query
              or 'when' in query or 'where' in query):
            speak("searching...")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("where", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

#open browser

        elif ("search" in query or "open website" in query):
            print("What should i search or open?")
            speak("What should i search or open?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
            quit()

#os related tasks
#sysytem logout/ shut down/restart

        elif ("sign out" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")

# screenshot
        elif ("screenshot" in query):
            screenshot()
            speak("Done!")

# cpu and battery usage
        elif ("cpu and battery usage" in query or "battery usage" in query
              or "cpu usage" in query):
            cpu()

#play songs

        elif ("play songs" in query):
            print("Opening music player...")
            speak("Playing...")
            songs_dir = "F:\\Music\\Hollywood"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[1]))
            quit()

#reminder function

        elif ("remind me" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            print("You said to remember  " + data)
            speak("You said to remember  " + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

#reading reminder list

        elif ("what was the reminder" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            print("You said me to remember that: " + reminder_file.read())
            speak("You said me to remember that: " + reminder_file.read())

# personal info
        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()

        #features
        elif ("your features" in query or "help" in query
              or "features" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can play songs,
            i can open any website,
            i can search things on wikipedia,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            and can change my voice too.
            tell me what can i do for you??
            '''
            print(features)
            speak(features)

        elif ("hii" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query):
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

#exit function

        elif ('bye bye' in query or 'bye' in query or 'nothing' in query):
            wishme_end()
