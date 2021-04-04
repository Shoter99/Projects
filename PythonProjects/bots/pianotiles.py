import pyautogui as pg
import keyboard as k
import win32api
import win32con
import time
pg.PAUSE = 0.01
t = 0
score = 300
m = 3


def click(x, y):

    global t, score, m
    if t > score and score < 1500:
        m += 0.05
        score += 50
    if t>score and score>1500:
        m+=0.2
        score += 50
    win32api.SetCursorPos((x, round(y+m)))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    t += 1


def press():
    if pg.pixel(426, 450)[2] <= 200:
        click(426, 450)
    if pg.pixel(481, 450)[2] <= 200:
        click(481, 450)
    if pg.pixel(546, 450)[2] <= 200:
        click(546, 450)
    if pg.pixel(627, 450)[2] <= 200:
        click(627, 450)


while not k.is_pressed('q'):
    try:
        press()
    except Exception as e:
        press()
