import mouse as mouse
import keyboard as kb
import time
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