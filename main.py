from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

# Timings
tabSwitchTime = 30
iterationsBeforeRefresh = 3

def mainLoop():
    while True:
        for i in range(iterationsBeforeRefresh):
            keyboard.press(Key.ctrl)
            keyboard.press(Key.page_down)
            keyboard.release(Key.ctrl)
            keyboard.release(Key.page_down)
            (time.sleep(tabSwitchTime))
        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release(Key.ctrl)
        keyboard.release('r')

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