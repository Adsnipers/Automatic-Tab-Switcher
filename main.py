from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

# Timings
tabSwitchTime = 30

def mainLoop():
    while True:
        keyboard.press(Key.ctrl)
        keyboard.press(Key.page_down)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.page_down)
        (time.sleep(tabSwitchTime))

def initDash():
    print("######################")
    print('Automatic Tab Switcher')
    print("----------------------")
    print(" By: Ashton Southall  ")
    print("######################")
    print()
    print('tabSwitchTime: ' + str(tabSwitchTime))
    print()
    print("Running...")

initDash()
mainLoop()