import speech_recognition as sr
# from pyautogui import click
# from instabot import bot
# from keyboard import *
import subprocess
import webbrowser
import wikipedia
import datetime
import pyttsx3
import pyjokes
import winshell
import random
import os




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    '''
    function for voice of saash
    '''
    engine.say(audio)
    engine.runAndWait()


def Greeting():
    '''
     this function wishes me good morning and good afternoon as per clock and ask how can saash help me
    '''
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Hello AAYUSH Sir Good Morning!")

    elif hour >= 12 and hour <= 18:
        speak("Hello AAYUSH Sir Good afternoon!")

    else:
        speak("Hello AAYUSH Sir Good evening!")

    speak("I am Saash,your voice assistant. Please tell me how may I help you")


def userinput():
    '''
    it take microphone input from user and return as string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        user_command = r.recognize_google(audio, language='en-in')
        print(f"user said:  {user_command}\n")

    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return user_command


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bgm.sanatan2@gmail.com', 'choco9785')
    server.send('bgm.sanatan2@gmail.com ', to, content)
    server.close()




# def YoutubeAuto():
#     while True:
#         query = userinput()

#         if 'pause' in query:
#             press('space bar')

#         elif 'resume' in query:
#             press('space bar')

#         elif 'full screen' in query:
#             press('f')

#         elif ' exit full screen' in query:
#             press('f')

#         elif 'film screen' in query:
#             press('t')

#         elif 'skip' in query:
#             press('l')

#         elif 'back' in query:
#             press('j')

#         elif 'mute' in query:
#             press('m')

#         elif 'unmute' in query:
#             press('m')

#         elif 'increase playback speed' in query:
#             press_and_release('SHIFT + .')

#         elif 'decrease playback speed' in query:
#             press_and_release('SHIFT +,')

#         elif 'previous' in query:
#             press_and_release('SHIFT + p')

#         elif 'next' in query:
#             press_and_release('SHIFT + n')

#         elif 'search' in query:
#             click(x=998, y=120)
#             speak("what to search")
#             search=user_command
#             write(search)
#             press('enter')

#         else:
#             speak('Command not found!')




    


if __name__ == "__main__":
    Greeting()
    while True:

        
        user_command = userinput().lower()
    # logic for executing task based on user_command
        if 'wikipedia' in user_command:
            speak("Searching Wikipedia...")
            user_command = user_command.replace("Wikipedia", "")
            result = wikipedia.summary(user_command, sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)
            


        elif 'how are you' in user_command:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'youtube' in user_command:
            url = "youtube.com"
            # YoutubeAuto() 


        elif 'google' in user_command:
            webbrowser.open("google.com")

        elif 'instagram' in user_command:
            webbrowser.open("instagram.com")

        elif 'whatsapp' in user_command:
            webbrowser.open("web.whatsapp.com")

        elif 'facebook' in user_command:
            webbrowser.open("facebook.com")

        elif 'linkedin' in user_command:
            webbrowser.open("linkedin.com")

        elif 'stack overflow' in user_command:
            webbrowser.open("stackoverflow.com")

        elif 'is love' in user_command:
            speak("It is 7th sense that destroy all other senses")

        elif "who made you" in user_command or "who created you" in user_command:
            speak("I was created as a Minor project by AAYUSH GARG ")

        elif 'joke' in user_command:
            speak(pyjokes.get_joke())

        elif 'music' in user_command:
            music_dir = 'D:\\Video\\Music'
            songs = os.listdir(music_dir)

            os.startfile(os.path.join(
                music_dir, songs[random.randint(0, len(songs))]))


        elif 'time' in user_command:

            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            speak(f"sir,the time is {current_time}")

        elif 'open vs code' in user_command:
            codePath = "C:\\Users\\AAYUSH GARG\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # elif 'email' in user_command:
        #     try:
        #         speak("What should I say?")
        #         content = userinput()
        #         to = "ashuflty@gmail.com"
        #         sendEmail(to, content)
                # speak("Email has been sent!")

            # except Exception as e:
            #     print(e)
            #     speak("Sorry my  friend aayush.I am not able to send this email")

        elif 'exit' in user_command:
            speak("Thanks for giving me your time")
            exit()


        elif 'empty recycle bin' in user_command:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "write a note" in user_command:
            speak("What should i write, sir")
            note = userinput()
            file_for_write = open('Saash.txt', 'w')
            file_for_write.write(note)
            file_for_write.close()



        elif "read note" in user_command:
            speak("Showing Notes")
            file_for_read = open("Saash.txt", "r")
            print(file_for_read.read())
            speak(file_for_read.read())
            file_for_read.close()

        elif 'shutdown' in user_command:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system("shutdown /s /t 1")

        elif 'restart' in user_command:
                speak("Hold On a Sec ! Your system is on its way to restarting")
                os.system("shutdown /r /t 1")