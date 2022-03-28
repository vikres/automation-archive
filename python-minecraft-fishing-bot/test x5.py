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
import pytesseract

time.sleep(2)
pydirectinput.click(1280,720)
time.sleep(0.05)
time.sleep(0.6)
pydirectinput.keyDown('s')
time.sleep(0.5)
pydirectinput.keyUp('s')
time.sleep(0.6)
pydirectinput.keyDown('a')
time.sleep(0.5)
pydirectinput.keyUp('a')
time.sleep(0.6)
pydirectinput.keyDown('w')
time.sleep(0.5)
pydirectinput.keyUp('w')
time.sleep(0.6)
pydirectinput.keyDown('w')
pydirectinput.press('space')
time.sleep(0.1)
pydirectinput.keyUp('w')  
time.sleep(0.3)
pydirectinput.keyDown('shift')
time.sleep(0.2)
pydirectinput.keyDown('w')
time.sleep(0.3)
pydirectinput.keyDown('a')
time.sleep(0.3)
pydirectinput.keyUp('w')
time.sleep(0.2)
pydirectinput.keyUp('a')
time.sleep(0.2)
pydirectinput.keyUp('Shift')
time.sleep(0.2)
pydirectinput.press('Shift')