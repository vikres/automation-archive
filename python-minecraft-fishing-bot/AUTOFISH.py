import pyautogui
from PIL import ImageGrab
from PIL import Image
import time
import cv2
import os
import numpy as np
import PySimpleGUI as sg
import threading
from functools import partial 


ROOT_PATH = './'      
def Launcher():      
    def print(line):      
        window['output'].update(line)      
    sg.ChangeLookAndFeel('Dark')      
    namesonly = [f for f in os.listdir(ROOT_PATH) if f.endswith('.py') ]      
    sg.SetOptions(element_padding=(0,0), button_element_size=(14,2), auto_size_buttons=False)      
    layout =  [[sg.SimpleButton(('STOP'), button_color=('white','firebrick3'))],      
                [sg.Text('', text_color='white', size=(20,1), key='output')]]      

    window = sg.Window('Floating Toolbar', layout, no_titlebar=True, keep_on_top=True, location=(-10, 500), size=(100,40))    
    while True:      
        (event, value) = window.read()      
        if event ==  'STOP':      
            exit()
            
def loopi():
    myScreenshot = pyautogui.screenshot()
    screenshot = ImageGrab.grab()
    screenshot.save(r'C:\Users\victo\Documents\bot\screenshot.png')
    im = cv2.imread(r'C:\Users\victo\Documents\bot\screenshot.png')
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    print((im == (233, 82, 67)).all(axis=-1).max())

threading.Thread(target=partial (loopi,)).start() 
Launcher() 


myScreenshot = pyautogui.screenshot()
screenshot = ImageGrab.grab()
screenshot.save(r'C:\Users\victo\Documents\bot\screenshot.png')
im = cv2.imread(r'C:\Users\victo\Documents\bot\screenshot.png')
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
print((im == (233, 82, 67)).all(axis=-1).max())