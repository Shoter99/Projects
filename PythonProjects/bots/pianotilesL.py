import pyautogui as pg
import keyboard as k
import time
import mouse as me
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
    me.move(x,round(y+m))
    me.click()


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
