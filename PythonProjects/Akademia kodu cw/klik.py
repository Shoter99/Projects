import time
import pyautogui as ag
import keyboard as kb
encoding = 'utf-8'
screenWidth, screenHeight = ag.size()
currentMouseX, currentMouseY = ag.position()

for i in range(0, 10):
    time.sleep(10)
    ag.write("Kocham Cie")
    ag.press('enter')
