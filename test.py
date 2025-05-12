import speech_recognition as sr
import pyttsx3


myname = "Jarvis"
url = "https://google.com/search?q="
r = sr.Recognizer()
engine = pyttsx3.init()

def speak():
    engine.say('Hello sir, how may I help you, sir.')
    engine.runAndWait()


def listenme():
	with sr.Microphone() as source:
		audio = r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	try:
		print(r.recognize_google(audio))
		# reload(todaydate)
		return(r.recognize_google(audio))
	except:
		print("Couldn't Hear!")
		return(listenme())

if __name__ == "__main__":
    while True:
        result = listenme()
        if result:
            speak()
            break
