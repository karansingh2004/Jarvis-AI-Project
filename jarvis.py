from datetime import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import wikipedia
import webbrowser
import string
import os
import random
import datetime
import smtplib
from pytube import YouTube
import urllib.request


# Function to send mail but first u have to allow it to send mail by less secure methods
def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('enter-mail-here' , 'enter-password-here')
    server.sendmail('enter-reciver-mail' , to, content)
    server.close()
    

#Function for speaking voice 
def speak(audio):
    myobj=gTTS(text=audio,lang='en',slow=True)
    myobj.save("welcome1.mp3")
    playsound("welcome1.mp3")
    
    
def takeCommand():
    # It takes microphone input and return text....
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said : {query.lower()}\n")

    except Exception as e:
        print("Say that Again pls...")
        speak("Dubara Bolyie...")
        return "none"

    return query


if __name__ == '__main__':
    speak("Ram Ram Karan.")
    while True:
        query=takeCommand().lower()

    # logic based on query to execute tasks
    

        # Function to search something on wikipedia
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query=query.replace("wikipedia", "")
            wiki_sum = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia....\n")
            print(wiki_sum)
            speak(wiki_sum)
        
        
        #Function to play Music but remember to give it proper path    
        elif 'music' in query:
            music_dir='/home/barryallen/Desktop/ubuntudesktop/jarvis_ke_gane' 
            # Enter path of folder which store the songs u want to play
            songs=os.listdir(music_dir)
            # print(songs)

            #To play any random songs 
            i=random.randint(1,87)
            print(f"<><><><><> {songs[i]} <<<{i}>>> <>><><>><>")
            playsound(f'{music_dir}/{songs[i]}')
            

        # Function to tell about the time     
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H : %M : %S ")
            print(strTime) 
            speak(strTime)
            
        # Function to open VSCode window    
        elif 'code' in query:
            # path="/home/barryallen/snap/code/94/usr/share/code/code"
            action='code'
            os.system(action)


            
        elif 'send email to me' in query:
            try:
                speak("What Should I say ?")
                content=takeCommand()
                to="reciver-mail-id"
                sendMail(to, content)
                speak("Mail is sent")
                
            except Exception as e:
                print(e)
                speak("Sorry, Mail could not be send")
        
        

        #Function to search something on youtube
        elif 'search on youtube' in query:

            #speak the text u want to search on youtube
            str= takeCommand().lower()       
            url_str = urllib.parse.quote(str)
       
            url= f"https://www.youtube.com/results?search_query="+url_str
            webbrowser.open(url)

            # html = urllib.request.urlopen(url)
            # print(html.read().decode())


#              <><><> YouTube Video Downloader <><><>
            #Put link of any youtube video here and also can adjust the resolution. It will download it
            link = #enter any youtube video link here
            video=YouTube(link)
            stream=video.streams.get_highest_resolution()
            stream.download()


        # Search something on google
        elif 'search on google' in query:
            # Speak What u want to search on google
            str= takeCommand().lower()
            url_str = urllib.parse.quote(str)    # Make ur word into url format

            url=f"https://www.google.com/search?q="+url_str  # Adding ur word with google url
            webbrowser.open(url)                            # Opening thar url
            
# Coded By - Karan Singh
