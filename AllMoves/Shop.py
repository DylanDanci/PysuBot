import mouse as mouse
import keyboard as kb
import time
kb.send("p")
mouse.move(600, 400, absolute=True, duration=0)
time.sleep(1)
mouse.press(button='right')
time.sleep(0.5)
mouse.release(button='right')
time.sleep(0.3)
kb.send("p")