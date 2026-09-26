# automation-archive

Scripts I wrote years ago to "cheat" in games. used opencv tech: screenshots laptop, cleans screenshot out, identifies what is on it to do actions on my behalf (i.e a bot). used ahk to control keyboard and scan screen,.. 

## python-minecraft-fishing-bot

A Python bot that automated repetitive tasks on a Minecraft MMO server. It captures the screen continuously, detects an on-screen signal with a NumPy colour mask (frames loaded via OpenCV) and responds through DirectInput-level input (pydirectinput). A threaded timer switches it between two routines. Delays are drawn from a truncated normal distribution, so the timing stays irregular, and the bot shuts itself down when the signal stops appearing. fishing_bot.py is the latest version, and AUTOFISH.py adds a PySimpleGUI stop button.

## keyboard-python-macros

AutoHotkey scripts for repetitive input: key-hold toggles, clickers on randomised intervals and timed multi-key sequences. The largest takes a target count and a screen region marked with two hotkeys. It scans that region with PixelSearch, clicks each match with a random offset, returns the cursor to where it was and stops once the count is reached.

## page-web-random

random bad test
