from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
def main():
    while True:
        keyboard.press(Key.ctrl)
        keyboard.press(Key.page_down)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.page_down)
        time.sleep(30)

def timedReload():
    while True:
        keyboard.tap(Key.f5)
        time.sleep(1800)

main()
timedReload()
