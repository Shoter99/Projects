import keyboard
import pyautogui as pg
from multiprocessing import Process
from mss import mss
import numpy as np
import time

sct = mss()

g = {'left':408, 'top':579, 'width':1, 'height':1}
r = {'left':605, 'top':581, 'width':1, 'height':1}
y = {'left':309, 'top':727, 'width':1, 'height':1}
b = {'left':650, 'top':735, 'width':1, 'height':1}

cords = {
        'green':(408,579),
        'red':(605,581),
        'yellow':(309,727),
        'blue':(650,735)
        }

result = []
level = 1;

def detect():
    detecting = False
    while True:
        time.sleep(.1)
        g_pix = np.array(sct.grab(g))
        r_pix = np.array(sct.grab(r))
        y_pix = np.array(sct.grab(y))
        b_pix = np.array(sct.grab(b))
        #print(g_pix[0][0][0], r_pix[0][0][0],y_pix[0][0][0],b_pix[0][0][0])
        if not detecting and \
                g_pix[0][0][0] == 102 and \
                r_pix[0][0][0] == 4 and \
                y_pix[0][0][0] == 23 and \
                b_pix[0][0][0] == 166:
                    detecting = True
        if not detecting:
            continue
        if g_pix[0][0][0] != 102:
            return 'green'
            break
        if r_pix[0][0][0] != 4:
            return 'red'
            break
        if y_pix[0][0][0] != 23:
            return 'yellow'
            break
        if b_pix[0][0][0] != 166:
            return 'blue'
            break
def score(result):
    for i in result:
       time.sleep(.1)
       x,y = cords[i]
       pg.click(x,y)



while keyboard.is_pressed('q') == False:
    print(level)
    for i in range (level):
        res = detect()
        result.append(res)
        print(res, i)
        
    level+=1
    print(result)
    time.sleep(.5)
    score(result)
    result = []
