import random
import time
from pydirectinput import press, keyDown, keyUp, typewrite
from pywinauto import application
from pywinauto.findwindows import find_window, WindowNotFoundError
from keyboard import write #pyautogui wont type special characters so gotta use this loll


window_name = input("Enter the name of the application as seen in Task Manager: ")
chat_indicator = input("Enter chat indicator (eg. '/', 't', etc.): ")
doJump = input("Would you like to enable doJump? (Y/N) ")
if doJump == "Y" or "y":
    doJump = True
elif doJump == "N" or "n":
    doJump = False
else:
    print("Please enter (Y/N) for dojump.")
    exit()
print(window_name)
try:
    window_handle = find_window(title_re=window_name)
    app = application.Application().connect(handle=window_handle)
    window = app.window(handle=window_handle)
    window.maximize()
    window.set_focus()
    
    print(f"{window_name} has been maximized and focused.")
except WindowNotFoundError:
    print(f"{window_name} not found!")
    exit()

phrases=["Hey!", "I'm a bot! 😁", ":D", "What's up!", "Who, me?", "🧃🌎", "I'm heartless! 😆 Get it?", "Updating..."]

prevkeystroke = 0 #this really !!helps with not having the same keystroke 4 times in a row
prevphrasetosay = "" #same as prevkeystroke

def presskey(keystroke):
    keyInterval = random.uniform(.2, 2)

    if keystroke == 1:
        keyDown('w')
        time.sleep(keyInterval)
        keyUp('w')
    elif keystroke == 2:
        keyDown('a')
        time.sleep(keyInterval)
        keyUp('a')
    elif keystroke == 3:
        keyDown('s')
        time.sleep(keyInterval)
        keyUp('s')
    elif keystroke == 4:
        keyDown('d')
        time.sleep(keyInterval)
        keyUp('d')
    elif keystroke == 5:
        keyDown('w')
        keyDown('a')
        time.sleep(keyInterval)
        keyUp('w')
        keyUp('a')
    elif keystroke == 6:
        keyDown('w')
        keyDown('d')
        time.sleep(keyInterval)
        keyUp('w')
        keyUp('d')
    elif keystroke == 7:
        keyDown('s')
        keyDown('d')
        time.sleep(keyInterval)
        keyUp('s')
        keyUp('d')
    elif keystroke == 8:
        keyDown('s')
        keyDown('a')
        time.sleep(keyInterval)
        keyUp('s')
        keyUp('a')
    elif keystroke == 10:
        press('space')

while True:
    time.sleep(1) #every ___ seconds we 'run it' as the kids say

    keyChance = .50 #50% chance to select a keystroke
    if random.random() < keyChance:

        space_chance = .1 #10% chance to press space (or select 10)

        keystroke = random.randrange(1, 8)
        if random.random() < space_chance: #set to jump (10)
            keystroke = 10

        if keystroke != prevkeystroke:
            presskey(keystroke)
            prevkeystroke = keystroke
        else:
            while keystroke == prevkeystroke:
                keystroke = random.randrange(1, 8)
            presskey(keystroke)
            prevkeystroke = keystroke
    
    phraseChance = .10 #10% chance to type in chat
    if random.random() < phraseChance:
        phraseToSay = random.choice(phrases)
        if phraseToSay != prevphrasetosay:
            keyDown(chat_indicator) #look, idk why i have to do this instead of "press" :(
            keyUp(chat_indicator)
            time.sleep(.05)
            write(phraseToSay)
            time.sleep(.05)
            keyDown('enter')
            keyUp('enter')
            prevphrasetosay = phraseToSay
        else:
            while phraseToSay == prevphrasetosay:
                phraseToSay = random.choice(phrases)
            keyDown(chat_indicator)
            keyUp(chat_indicator)
            time.sleep(.05)
            write(phraseToSay)
            time.sleep(.05)
            keyDown('enter')
            keyUp('enter')
            prevphrasetosay = phraseToSay
