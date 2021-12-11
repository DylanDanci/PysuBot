import mouse as mouse
import keyboard as kb
import time
time.sleep(0.1)
mouse.click(button='right')
time.sleep(0.1)
kb.press("F4")
mouse.move(800, 560, absolute=True, duration=0)
mouse.press(button='right')