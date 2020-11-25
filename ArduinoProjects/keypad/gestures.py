import serial as s
import time as t
import pyautogui as pg
import getpass
import os
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


ArduinoSerial = s.Serial('com4', 9600)
t.sleep(2)

while 1:
    incoming = str(ArduinoSerial.readline())
    print(incoming)

    if 'VolumeDown' in incoming:
        pg.press('volumedown')
    if 'VolumeUp' in incoming:
        pg.press('volumeup')
    if 'Forward' in incoming:
        pg.press('right')
    if 'Rewind' in incoming:
        pg.press('left')
    if 'Play/Pause' in incoming:
        pg.press('space')
    if 'Music' in incoming:
        pg.press('playpause')
    if 'Next' in incoming:
        pg.press('nexttrack')
    if 'Previous' in incoming:
        pg.press('prevtrack')
    if 'Win' in incoming:
        os.system('shutdown /s /t 10')
    if 'Sleep' in incoming:
        os.system('shutdown /a')
    if 'CMD' in incoming:
        os.system('start cmd')
    if 'MUTED' in incoming:
        pg.hotkey('ctrl','shift','m')    
    incoming = ""
