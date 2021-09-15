import pyttsx3
import speech_recognition as spe
import pywhatkit
import datetime as dt

listener = spe.Recognizer()
audio = pyttsx3.init()

# make alexa repeat what u say


def talk(speech):
    audio.say(speech)
    audio.runAndWait()


def take_command():
    try:
        with spe.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print('listening amigo...')
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            if 'mate' in cmd:
                cmd = cmd.replace('mate', '')
                print(voice)
    finally:
        print('cannot hear u mate')
    return cmd


def run_command():
    cmd = "what's the time mate?"
    if 'play' in cmd:
        music = cmd.replace('play', '')
        talk('talking'+cmd)
        pywhatkit.playonyt(music)
    elif 'time' in cmd:
        current_time = dt.datetime.now().strftime('%I:%M%p')
        talk(current_time)


run_command()
