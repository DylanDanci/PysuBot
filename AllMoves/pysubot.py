import keyboard as kb
import mouse as mouse
import time
import speech_recognition as sr
from playsound import playsound
recognizer_instance = sr.Recognizer()
with sr.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    print("Sono in ascolto... parla pure!")
    audio = recognizer_instance.listen(source)
    print("Ok! sto ora elaborando il messaggio!")
try:
    text = recognizer_instance.recognize_google(audio, language="it-IT, en-EN")
    print(text)
except Exception as e:
    print(e)
text = 'Pisu'
if text in ['Pisu']:
    power = True
while(power == True):
    recognizer_instance = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source)
        print("Sono in ascolto... parla pure!")
        audio = recognizer_instance.listen(source)
        print("Ok! sto ora elaborando il messaggio!")
        try:
            text = recognizer_instance.recognize_google(audio, language="it-IT, en-EN")
            print(text)
        except Exception as e:
            print(e)
    if text in ['Pisu Addio']:
        power = False
    if text in ['Compra']:
        kb.send("p")
        mouse.move(600, 400, absolute=True, duration=0)
        time.sleep(1)
        mouse.press(button='right')
        time.sleep(0.5)
        mouse.release(button='right')
        time.sleep(0.3)
        kb.send("p")
    if text in ['Segui']:
        time.sleep(0.1)
        mouse.click(button='right')
        time.sleep(0.1)
        kb.press("F4")
        mouse.move(800, 560, absolute=True, duration=0)
        mouse.press(button='right')
    if text in ['Base']:
        kb.send("b")
    if text in ['Scudo']:
        kb.press("F4")
        mouse.move(960, 540, absolute=True, duration=0)
        time.sleep(0.1)
        kb.send("E")
        time.sleep(0.1)
        mouse.move(800, 560, absolute=True, duration=0)
        time.sleep(0.1)
        mouse.click(button='right')
        time.sleep(0.1)
        mouse.press(button='right')
    if text in ['Flash']:
        kb.send("F")
    if text in ['Cura']:
        kb.send("D")
    if text in ['Tornado']:
        mouse.press(button='right')
        kb.press("F4")
        mouse.move(1000, 400, absolute=True, duration=0)
        mouse.press(button='right')
        time.sleep(0.1)
        kb.send("Q")
        time.sleep(0.1)
        kb.send("Q")
        mouse.move(800, 560, absolute=True, duration=0)
        time.sleep(0.1)
        mouse.click(button='right')
        time.sleep(0.1)
        mouse.press(button='right')
    if text in ['Via']:
        kb.send("S")
        time.sleep(0.1)
        kb.send("R")
        time.sleep(3)
        kb.press("F4")
        mouse.move(800, 560, absolute=True, duration=0)
        time.sleep(0.1)
        mouse.click(button='right')
        time.sleep(0.1)
        mouse.press(button='right')
    