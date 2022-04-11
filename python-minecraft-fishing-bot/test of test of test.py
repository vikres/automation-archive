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
mouse = pynput.mouse.Controller()
time.sleep(4)
connard = 0
while connard <= 300:
      pydirectinput.click() # click in the middle of the screen
      time.sleep(0.005)
      connard = connard + 1


#img = cv2.imread(r'C:\Users\victo\Documents\bot\screenshot.png')
#ind = np.where((img[:, :, 0]==85) & (img[:, :, 1]==255) & (img[:, :, 2]==85))
#answer = list(zip(ind[0], ind[1]))
#print(answer)
#if len(answer) >= 5:
#    print('success')