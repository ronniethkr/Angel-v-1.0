#use to text to speech conversion
import pyttsx3
import datetime
from time import sleep
import speech_recognition as sr
import os
import wikipedia
import wolframalpha
import sys
import threading
import numpy as np
import cv2
id="5LL4JQ-3Q3Y92EU7X"
client = wolframalpha.Client(id)
check=str()
time=str()
repeat1=str()
conversation=[]
count=0
a=str()
u=str()
C=int()

def shutup():
    q=myCommand()
    while "sorry angel" not  in q:
        q=myCommand()
    return

def detetct():
    speak("press escape for exit")
    def main():
        #name="priview"
        #cv2.namedWindow(name)
        #cv2.namedWindow(name1)
        cap=cv2.VideoCapture(0)

        if cap.isOpened():
            ret,frame=cap.read()
        else:
            ret=False

        while ret:

            ret,frame=cap.read()
            face_detection = cv2.CascadeClassifier('E://Python program//12. Detect Faces and Eyes//Haarcascades//haarcascade_frontalface_default.xml')
            faces = face_detection.detectMultiScale(frame, 1.1, 5)
            faces=np.asarray(faces)
            x=faces.shape
            z,y=(str(x)).split(',')
            z,y=z.split("(")
            y=str(y)
            print(y)
            if y>1:
                speak("i can see"+y+"persons there")
            elif y==1:
                Speak("only one person is there")
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), 3)
            cv2.imshow('Single Face Detection', frame)
            if cv2.waitKey(1)==27:
                break
        cv2.destroyAllWindows()
        cap.release()
    if __name__=="__main__":
        main()
def history():
    #print(count)
    #print(conversation)
    speak(conversation[-2])


def fortuneteller():
    answer ='yes'

    speak('Welcome to the Fortune Teller!')
    speak('You will select a color and a number and I will tell you what the future holds for you!')

    while answer =='yes':
        speak("Select a colour from yellow, green, blue, red")
        color=myCommand()
        color=color.lower()
        if color== "yellow" or color =="green":
            speak(" NOw Select a number from 1, 2, 5, 6")
            number=myCommand()

            if number == 'one'or number == '1':
                  speak("Worried about your future career? Don't worry. You'll 100% get what you want, be patient!")
            elif number == 'two' or number== '2':
                  speak("You will become a millionaire at the age of 35!")
            elif number == 'five' or number== '5':
                  speak("You will have a great family with 10 kids!")
            elif number == 'six' or number == '6':
                  speak("You will become famous and everyone will love you!")
            else:
                  speak("Numbers 1, 2, 5, 6 are the only numbers allowed")

        elif color == "blue" or color == "red":
            speak("Select a number from 3, 4, 7, 8")
            number=myCommand()
            if number == 'three' or number== '3':
                  speak("You will live a happy life for 100 years at least!")
            elif number == 'four'or number == '4':
                  speak("You will become a successful doctor one day!")
            elif number == 'seven'or number =='7':
                  speak("All your dreams will come true, just be patient!")
            elif number == 'eight' or number=='8':
                  speak("You're lucky, You will have it all one day!")
            else:
                  speak("Numbers 3, 4, 7, 8 are the only numbers allowed")
        else:
            speak("Colors [yellow, green, blue, red] are only allowed")
        speak("Play again?'yes'  or NO")
        answer=myCommand()
        answer=answer.lower()
        speak(answer)
        if answer=='no':
            speak('bye sir')
            speak("exiting from  fortune teller")
        elif answer=='yes':
            fortuneteller()
        else:
            speak("wrong entry  again entring in fortune teller")
            fortuneteller()


def reccords():
    global conversation
    global conversationcp

    x=count
    x=str(x)
    #Speak("you had ask me questions")
    speak("you want all the records of the conversation Boss")
    q=myCommand()
    if 'yes' in q:
        speak('okay')
        conversationcp=conversation
        print(conversation)

        newl=conversation
        check=0
        check2=2
        global c
        c=len(newl)
        print(c)
        while check!=c:
            newl.insert(check,'u say')
            check=check+4
            newl.insert(check2,'i say')
            check2=check2+4
            c=len(newl)
        print(newl)
        newl=str(newl)
        speak(newl)
        #conversation=list(dict.fromkeys(conversation)
        conversation=list(dict.fromkeys(conversation))
        conversation.remove('u say')
        conversation.remove('i say')
    elif 'no' in q:
        speak("okay")
    else:
        speak("you give wrong input boss")

def speak(audio):
    global count
    global conversation
    if count >=1:
        conversation.append(audio)
    repeat1=audio
    engine=pyttsx3.init("sapi5")
    engine = pyttsx3.init()
    rate= engine.getProperty('rate')
    rate1= engine.setProperty('rate',150)
    #print(rate)
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    #print ("volum= {}".format(volume))

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    #for female set it to 1;sc
    print("Angel:"+repeat1)
    engine.say(audio)
    engine.runAndWait()
    #print("length={}".format(len(voices)))


"""def check():
    engine=pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    for x in voices:
        print(x)"""


def greet():
    global time
    hour=datetime.datetime.now().hour
    minute=datetime.datetime.now().minute
    sec=datetime.datetime.now().second
    mint=minute
    """if hour >=13:
        hour=hour-12
    time=str(hour)+"  "+str(mint)+ "and"+str(sec)+"seconds"
    #speak(time )

    x=str(hour)+":"+str(minute)"""

    if hour >= 0 and hour < 12:
        speak('Good Morning BOss!')

    if hour >= 12 and hour < 18:
        speak('Good Afternoon Boss !')

    if hour >= 18 and hour !=0:
        speak('Good Evening Boss !')
#    print("The time is "+x)
    #speak("The time is")
    #speak(x)
greet()
#speak("Hello  Boss Angel is here")
#speak("whats the plan for today?")

count=1



def myCommand():
    global count
    count=count+1
    """query = str(input('Command: '))
    return query"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # listen for 1 second to calibrate the energy threshold for ambient noise levels
        #r.adjust_for_ambient_noise(source)
        print("listenning..................")
        r.pause_threshold =  0.4
        r.non_speaking_duration=0.1
        #r.pause_threshold=0.35
        audio=r.listen(source)
        #print(type(audio))

    try:
        query = r.recognize_google(audio, language='en-in')
        conversation.append(query)
        print('user: ' + query + '\n')
        return query
    except sr.UnknownValueError:
        speak("Sorry sir! I didnot get that! Try typing the command!")

        query = str(input('Command: '))
        conversation.append(query)
        return query
    except:

            speak("due to network fault faliure in my system")




if __name__=="__main__":

    while True:
        #try:
            q=myCommand()
            q=q.lower()
            if 'your name' in q:
                speak('angel')
            elif 'namaste' in q:
                speak('namaste ji')
            elif 'sat shiri akal' in q or 'sat siri akal'in q or 'sat sri akal' in q:
                speak('sat siri akaaal ji')
            elif 'hello' in q or 'hii' in q or 'hey' in q:
                speak('Hello Boss')
            elif 'jai sita ram' in q :
                speak('jai sita ram ji')
            elif 'kida' in q:
                speak("vadiaa boss tusi daso")
            elif 'your boss' in q:
                speak('mister Ronnie Thakur')
            elif 'who are you' in q:
                speak("i am Angel")
            elif 'how are you' in q:
                speak("I am fine Boss Thank you  what's about you")
            elif'fine' in q:
                speak("great Boss")
            elif "do you wanna harm me or not" in q:
                speak("if you harm me i will show you how to harm")
            elif 'from where do you came'in q:
                speak("from the brain of my BOss ")
            elif 'what you know about your boss' in q:
                speak("he is great perssonality and genius")
            elif 'from where are you' in q:
                speak("i am from earth ")
            elif 'whats the time angel' in q:
                speak("the time is " +time)
            elif 'your age' in q or "old are you" in q:
                speak("my age is 22 years old")
            elif 'shut up' in q:
                speak("oka")
                shutup()
            elif 'my fortune' in q:
                speak("okay")
                fortuneteller()
            elif 'repeat' in q:
                history()
            elif 'records angel' in q:
                reccords()
                #print(conversation)
            elif 'can you see me'in q:
                speak('Yes boss')
                detetct()
            elif 'nothing' in q or 'abort' in q or 'stop' in q or 'quit' in q or 'exit' in q:
                speak('okay')
                speak('Bye Sir, have a good day.')
                sys.exit()

            else:
                try:
                    try:
                        speak('wait let me think...')
                        res = client.query(q)
                        results = next(res.results).text
                        speak('Got it.')
                        speak('according to me - ')
                        speak(results)
                    except:
                        results = wikipedia.summary(q, sentences=2)
                        speak('Got it.')
                        speak('According to me - ')
                        speak(results)
                except:
                    speak("sorry sir this thing is not known by me")
        #except:
            #speak("there is technical issue please check out my control flow")



    #check()
