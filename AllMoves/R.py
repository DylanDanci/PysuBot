import mouse as mouse
import keyboard as kb
import time
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