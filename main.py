from pynput.keyboard import Key, Controller
import time

while True:
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press(Key.page_down)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.page_down)
    time.sleep(30)

