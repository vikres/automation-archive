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
valeurPOST = 0


def antiwatchdog(valeurPRE, modificationMEDIANE):
    random.seed()
    global valeurPOST
    valeurPOST = random.gauss(valeurPRE, modificationMEDIANE)


time.sleep(6)
fish = 0
antimacrohub = 0
while fish <= 10:
    huh = 0
    meh = 0
    antimacrohub = antimacrohub + 1
    pai.rightClick(1280,720)
    time.sleep(.5)
    pai.keyDown('alt')
    time.sleep(.2)
    pai.press('tab')
    time.sleep(.2)
    pai.keyUp('alt')
    while huh <= 28:
        screenshot = ImageGrab.grab() 
        meh = meh + 1
      #  os.rename(r"C:\Users\victo\Documents\bot\screenshot.png",r"C:\Users\victo\Documents\bot\zscreenshot{}.png".format(meh))
        screenshot.save(r'C:\Users\victo\Documents\bot\screenshot.png')
        img = cv2.imread(r'C:\Users\victo\Documents\bot\screenshot.png')
        ind = np.where((img[:, :, 0]==54) & (img[:, :, 1]==69) & (img[:, :, 2]==255))
        answer = list(zip(ind[0], ind[1]))
        print(answer)
        if len(answer) >= 5:
            print('pulling rod...')
            break
        else:
            huh = huh + 1
        print(f"scanning for the red mark for the {huh}'s time..")
    time.sleep(0.4)
    pai.rightClick(1280,720)
    time.sleep(1)
    fish = fish + 1
    if antimacrohub >= 3:
        antimacrohub = 0
        im = Image.open(r'C:\Users\victo\Documents\bot\screenshot.png') # Can be many different formats.
        pix = im.load()
        if pix[2359,658] != (85, 255, 85):
            print('not on island, breaking script')
            break
        else:
            print('still in the island, perfect!')
        

