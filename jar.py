## Jarvis mark 1
import os 
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pyttsx3
import datetime

opts = {
    "alias": ('джарвис', 'жарвис', 'жар', 'джарвис', 'арвис'),
    "tbr": ("скажи", "раскажи", "покажи", "сколько", "произнеси"),
    "cmds": {
        "ctime": ("текущее время", "сейчас времени", "который час", "времени"),
        "radio": ("включи музыку", "воспроизведи радио","включи радио"),
        "stupid1": ("расскажи анекдот", "расмеши меня", "ты знаешт анектод")
    }
}

# Фунции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Jarvisy
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            
            # распознаем команду и выполняем ее
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])


    except sr.UnknownValueError:
        print("[log] голос не распознан!")
    except sr.RequestError:
        print("[log] Неизсвестная ошибка, проверте интернет !")

def recognize_cmd(cmd):
    RC = {'cmd':'', 'percent':0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC

def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    elif cmd == 'radio':
        # воспроизвести радио
        os.system("d:\\jarvis\\res\\radio_record.mp3")
    elif cmd == 'stupid1':
        #Расказать анекдот
        speak("Мой создатель не научил меня анектодам")
    else:
        print("Команда не разопознана")


# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)


speak_engine = pyttsx3.init()

# Только если у вам остановлены голоса для синтеза речи!
##voices = speak_engine.getProperty('voices')
#speak_engine.setProperty('voice', voices.id)

speak("Добрый день, создатель")
speak("Джарвис на связи")

stop_listenining = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # ifinity loop






##import speech_recognition as sr
##
##r = sr.Recognizer()
##with sr.Microphone(device_index=1) as source:
##    print("Скажите что нибудь ...")
##    audio = r.listen(source)
##
##query = r.recognize_google(audio, language="ru-RU")
##print('Вы сказали: ' + query.lower())