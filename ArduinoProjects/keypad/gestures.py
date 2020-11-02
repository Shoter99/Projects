import serial as s
import time as t
from pyautogui import alert, typewrite

ArduinoSerial = s.Serial('ttyACM1',9600)
t.sleep(2)

while 1:
    incoming = str(ArduinoSerial.readline())
    print(incoming)

    if 'VolumeDown' in incoming:
        alert('Wcisnieto')
    incoming = ""