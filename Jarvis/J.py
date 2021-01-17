import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import translators as ts
import pickle

re = {'deepanshu': 'deepanshug40@gmail.com', 'sonu': 'sonu87670@gmail.com'}
la = {'french': 'fr', 'hindi': 'hi', 'german': 'de'}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', 'voices[0].id')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour <= 16:
        speak("Good Afternoon")
    elif hour > 16 and hour <= 19:
        speak("Good Morning")
    else:
        speak("Good Night")

    speak("I'm Jarvis. How may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognising")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said {query}")

    except Exception as e:
        print("Say that again please")
        return "None"
    
    return query.lower()

def sendEmail(receiver, content):
    your_email = os.environ.get('EMAIL_USER')
    your_password = os.environ.get('EMAIL_PASS')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(your_email, your_password)
    server.sendmail(your_email, receiver, content)

def trans(content, lang):
    translation = ts.google(content, to_language = lang)
    print(translation)
    speak(translation)
    # engine.setProperty('voice', 'voices[0].id')

def checkLang(query):
    for key in la.keys():
        if key in query:
            return la[key]
    else:
        return 0

def addMail(name, mail):
    if name in re.keys() and re[name] == mail:
        speak("Same contact exits. No changes made.")
    elif name in re.keys() and re[name] != mail:
        speak('Person exists. Do you want to change the contact or add a new one with a different name')
        if 'change' in takeCommand():    
            re[name] = mail
            speak('changes done')
        elif 'new' in takeCommand():
            speak('Please tell the new name')
            name = takeCommand()
            re[name] = mail
            speak("Person Added")
        else:
            speak('Please try again')
            exit()
    else:
            re[name] = mail
            speak("Person Added")
    print(re)

def createML():
    print("What is the name of the person")
    name = takeCommand()
    print("What is the mailing I'd? \nDo you want to type it or speak it")
    if "type" in takeCommand():
        mail = input()
    elif "speak" in takeCommand():
        mail = takeCommand()
        mail = mail.replace(" ", "")
    else:
        speak('please try again')
        exit()
    re = {}
    re[name] = mail
    file = 'maills.pkl'
    fileobj = open(file, wb)
    pickle.dump(re, fileobj)
    
    speak("Do you want to add more?")
    if 'yes' in takeCommand():
        print("What is the name of the person")
        name = takeCommand()
        print("What is the mailing I'd? \nDo you want to type it or speak it")
        if "type" in takeCommand():
            mail = input()
        elif "speak" in takeCommand():
            mail = takeCommand()
            mail = mail.replace(" ", "")
        else:
            speak('please try again')
            exit()

      

if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand()
        # query = 'add mailing contacts'
        query = query.lower()
        if 'wikipedia' in query :
            res = checkLang(query)
            if res:
                speak("Searching Wikipedia")
                query = query.replace('according to wikipedia', "")
                results = wikipedia.summary(query, sentences = 2)
                results = "According to Wikipedia. " + results
                trans(results, res)

            else:
                speak("Searching Wikipedia")
                query = query.replace('according to wikipedia', "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                speak(results)

        elif 'youtube' in query:
            webbrowser.open('youtube.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Deepanshu\\Desktop\\python\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "time" in query:
            gtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {gtime}")
        
        elif "open" in query and "visual code" in query:
            cpath = '"C:\\Users\\Deepanshu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            speak("opening visual studio")
            os.startfile(cpath)

        elif "email" in query:
            try:
                speak("What should I say?")
                content = takeCommand().capitalize()
                speak("Whom should I send it to?")
                receive = takecommand()
                receiver = re[receive]
                speak("sending the email")
                sendEmail(receiver, content)
                speak("Email is sent!")
            except Exception as e:
                speak('There\'s some error in sending the mail. Try again')
                print(e)
        
        elif "translate" in query:
            speak("In which language do you want to convert the text")
            lang = takecommand()
            query = query.replace("translate", " ")
            trans(query, la[lang])

        elif "add mailing contacts" or 'add contacts' in query:
            print("What is the name of the person")
            name = takeCommand()
            print("What is the mailing I'd? \nDo you want to type it or speak it")
            if "type" in takeCommand():
                mail = input()
            elif "speak" in takeCommand():
                mail = takeCommand()
                mail = mail.replace(" ", "")
            else:
                speak('please try again')
                exit()
            addMail('deepansu', 'deepanshug0@gmail.com')

        elif "create mailing list" in query:
            createML()

        else:
            speak("Exiting")
            exit()


