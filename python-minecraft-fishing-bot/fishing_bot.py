# Instructions: Get a small app (folder,...) so that alt tab will focus in this tab while the rod is cast. it should take the least amount of screen possible 


import pyautogui as pai
from PIL import ImageGrab
from PIL import Image
import time
import cv2
import os
import numpy as np
import threading
import time, traceback
import pydirectinput
import pynput
import random
valeurPOST = -1000
random.seed()


def antiwatchdog(valeurPRE, modificationMEDIANE):
    global valeurPOST
    for _ in range(1000):
        valeurPOST = -1000
        while ((valeurPOST<=valeurPRE - modificationMEDIANE) or valeurPOST>=valeurPRE + modificationMEDIANE):
            valeurPOST = random.gauss(valeurPRE, modificationMEDIANE)


#internal clock

def every(delay, task):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
      task()
    except Exception:
      traceback.print_exc()
      # in production code you might want to have this instead of course:
      # logger.exception("Problem while executing repetitive task.")
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // delay * delay + delay

timetokill = 0

def foo():
  print("Internal clock:", time.time())
  global timetokill
  timetokill = 1

time.sleep(4)
def zebi():
    global timetokill
    global valeurPOST
    global antimacrohub
    time.sleep(.5)
    pydirectinput.keyDown('shiftleft')
    pydirectinput.keyDown('shiftright')
    antiwatchdog(.2,.1),time.sleep(valeurPOST)
    pydirectinput.keyDown('s')
    time.sleep(0.05)
    pydirectinput.keyUp('s')
    antiwatchdog(.2,.1),time.sleep(valeurPOST)
    pydirectinput.keyUp('shiftleft')
    pydirectinput.keyUp('shiftright')
    antiwatchdog(.2,.1),time.sleep(valeurPOST)
    pydirectinput.press('Shift')
    fish = 0
    huh = 0
    didntfindredmark = 0
    antimacrohub = 0
    while timetokill == 0:
        meh = 0
        print(didntfindredmark)
        if huh >= 45:
            didntfindredmark = didntfindredmark + 1
        else:
            didntfindredmark = 0
        huh = 0
        if didntfindredmark >= 3:
            print('Not facing lava (went back to hub or got griefed), terminating script to avoid reports/ban')
            quit()
        antimacrohub = antimacrohub + 1
        antiwatchdog(.4,.1),time.sleep(valeurPOST)
        print('debug1')
        pydirectinput.rightClick(1280,720)
        time.sleep(.5)
        pai.keyDown('alt')
        time.sleep(.2)
        pai.press('tab')
        time.sleep(.2)
        pai.keyUp('alt')
        answer = ""
        while huh <= 45:
            myScreenshot = pai.screenshot() # screenshot your screen
            screenshot = ImageGrab.grab()
            meh = meh + 1
          #  os.rename(r"C:\Users\victo\Documents\bot\screenshot.png",r"C:\Users\victo\Documents\bot\zscreenshot{}.png".format(meh))
            screenshot.save(r'C:\Users\victo\Documents\bot\screenshot.png') # directory to choose where image analysis will be done
            img = cv2.imread(r'C:\Users\victo\Documents\bot\screenshot.png') # directory to choose where image analysis will be done
            ind = np.where((img[:, :, 0]==54) & (img[:, :, 1]==69) & (img[:, :, 2]==255)) # checks for pixel color of red mark
            ind = np.where((img[:, :, 0]==53) & (img[:, :, 1]==68) & (img[:, :, 2]==252)) # checks for pixel color of red mark
            answer = list(zip(ind[0], ind[1]))
        #    print(answer)
            if len(answer) >= 5: # pixel color found
                print('pulling rod...')
                break
            else:
                huh = huh + 1
          #  print(f"scanning for the red mark for the {huh}'s time..")
        time.sleep(.15)
        print('debug2')
        pydirectinput.rightClick(1280,720) # Right click in the middle of the screen - first rod cast 
        antiwatchdog(1,.2),time.sleep(valeurPOST)
        if antimacrohub >= 3:
            antimacrohub = 0
            im = Image.open(r'C:\Users\victo\Documents\bot\screenshot.png') # directory to choose where image analysis will be done
            pix = im.load()
            print('move camera and check island')
            antiwatchdog(.4,.07),time.sleep(valeurPOST)
            pydirectinput.press('space')
           # mouse = pynput.mouse.Controller()
           # randompos = random.randint(95,100)
           # randompos2 = random.randint(50,55)
           # mouse.move(randompos2, randompos) # moves to keep getting xp 
            antiwatchdog(.4,.1),time.sleep(valeurPOST)
           # mouse.move(-randompos2, -randompos)
        #detects in crystal h    if pix[57,76] != (43, 182, 115):
         #       print('not on island, breaking script')
         #       break
          #  else:
           #     print('still in the island, perfect!')
    print('TIME TO KILL!')
    antimacrohub = 0
    bitee = 0
    mouse = pynput.mouse.Controller()
    randomposREMINDER = random.randint(120,131)
    mouse.move(0, randomposREMINDER)
    threading.Thread(target = clicker).start()
    while bitee <= 2:
        bitee = bitee + 1
        antiwatchdog(.15,.04),time.sleep(valeurPOST)
        pydirectinput.keyDown('s')
        antiwatchdog(1.1,.06),time.sleep(valeurPOST)
        pydirectinput.keyUp('s')
        antiwatchdog(.15,.05),time.sleep(valeurPOST)
        pydirectinput.keyDown('Shift')
        pydirectinput.keyDown('d')
        antiwatchdog(.4,.07),time.sleep(valeurPOST)
        pydirectinput.keyUp('d')
        antiwatchdog(.4,.07),time.sleep(valeurPOST)
        pydirectinput.keyDown('w')
        antiwatchdog(.15,.04),time.sleep(valeurPOST)
        pydirectinput.keyUp('w')
      #  mouse = pynput.mouse.Controller()
      #  randompos = random.randint(90,95)
      #  randompos2 = random.randint(60,70) 
      #  mouse.move(randompos2, randompos) # moves to keep getting xp
        antiwatchdog(.2,.04),time.sleep(valeurPOST)
        pydirectinput.keyDown('a')
        antiwatchdog(.6,.07),time.sleep(valeurPOST)
        pydirectinput.keyUp('a')
        pydirectinput.keyUp('Shift')
      #  mouse.move(-randompos2, -randompos)
    antiwatchdog(1,.07),time.sleep(valeurPOST)
    mouse = pynput.mouse.Controller()
    mouse.move(0, -randomposREMINDER)

def clicker():
    global timetokill
    global valeurPOST
    global antimacrohub
    if timetokill == 1:
        connard = 0
        pydirectinput.press('2') # change to weapon in slot 2
        while connard <= 37: # 37 for giant sword
            pydirectinput.click(1280,720) # click in the middle of the screen
            antiwatchdog(.04,.01),time.sleep(valeurPOST)
            connard = connard + 1
        print('debug3')
        pydirectinput.rightClick(1280,720)
        pydirectinput.press('3') # change back to rod in slot 3
        time.sleep(2)
        pydirectinput.click(1280,720)
        time.sleep(0.6)
        pydirectinput.keyDown('s')
        antiwatchdog(.6,.1),time.sleep(valeurPOST)
        pydirectinput.keyUp('s')
        antiwatchdog(.4,.1),time.sleep(valeurPOST)
        pydirectinput.keyDown('a')
        antiwatchdog(.6,.1),time.sleep(valeurPOST)
        pydirectinput.keyUp('a')
        antiwatchdog(.4,.1),time.sleep(valeurPOST)
        pydirectinput.keyDown('w')
        antiwatchdog(.5,.1),time.sleep(valeurPOST)
        pydirectinput.keyUp('w')
        antiwatchdog(.1 ,.1),time.sleep(valeurPOST)
        pydirectinput.keyDown('w')
        pydirectinput.press('space')
        antiwatchdog(.1,.01),time.sleep(valeurPOST)
        pydirectinput.keyDown('shift')
        antiwatchdog(.2,.05),time.sleep(valeurPOST)
        pydirectinput.keyDown('w')
        antiwatchdog(.2,.05),time.sleep(valeurPOST)
        pydirectinput.keyDown('a')
        antiwatchdog(.22,.05),time.sleep(valeurPOST)
        pydirectinput.keyUp('w')
        antiwatchdog(.2,.1),time.sleep(valeurPOST)
        pydirectinput.keyUp('a')
        antiwatchdog(.2,.1),time.sleep(valeurPOST)
        pydirectinput.keyUp('Shift')
        antiwatchdog(.2,.1),time.sleep(valeurPOST)
        pydirectinput.press('Shift')
        antiwatchdog(.4,.1),time.sleep(valeurPOST)
        timetokill = 0
        threading.Thread(target = zebi).start()

threading.Thread(target=lambda: every(100, foo)).start()
zebi()