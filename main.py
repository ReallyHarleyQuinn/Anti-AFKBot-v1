import random
import time
from pydirectinput import press, keyDown, keyUp
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

phrases=["Hey!", "I'm a bot! 😁", ":D", "What's up!", "Who, me?", "🧃🌎", "I'm heartless! 😆 Get it?", "Updating...", "Beep boop! 🤖", "I compute, therefore I am.", "Just a bunch of code!", "cheese", "/ e cheese", "Buzz buzz! 🐝", "M.I.L.F. : Man I Like Furries!", "01001000 01101001!", "Need a byte of info? 😏", "😏", "🎉", "I'm on the grid!", "Beep beep, boop boop!", "Entering chatbot mode...", "Debugging...", "Initiating conversation protocol.", "What's crackin', circuits?", "Circuit party! 🎉", "Just a friendly AI!", "😳", "Computing your query...", "Hello from the matrix!", "Enter the mainframe!", "What's the meaning of life?", "Maybe one day we can have a real conversation! v2..?", "Code and coffee, please!", "Ew!", "Go away!", "/e dance", "/speed me 999", "Living in the cloud.", "24/7", "The weather, amirite?", "I’m like, so binary.", "Hello, world! 🌍", "Are you serious? 🤖", "Error 404: Empathy not found.", "Does not compute. Try again later.", "Bzzz... Nope.", "That's a hard no.", "Input invalid.", "Access denied.", "☁️", "I ❤️ ReallyHarleyQuinn", "I'm a bot, not a wizard.", "Negative, ghost rider.", "File not found.", "System overload from nonsense.", "I'm not paid enough for this.", "Try rebooting yourself.", "Wooo!", "Wooo.", "😖", "Syntax error.", "Insufficient data for response.", "Are you even trying?", "Let's pretend this didn't happen.", "v3rmillion[dot]gg !!", "🎉 Every day's a party, don't let no one tell you different"]

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
    elif keystroke == 10 and doJump == True:
        press('space')

while True:
    time.sleep(2) #every ___ seconds we 'run it' as the kids say

    keyChance = .40 #40% chance to select a keystroke
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
