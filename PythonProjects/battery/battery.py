from  pip._internal import  main
main(["install", "psutil"])
import ctypes, psutil, time

battery = psutil.sensors_battery()
while True:
    battery = psutil.sensors_battery()
    if battery.power_plugged:
        time.sleep(5)
    else:
        if battery.percent <= 15:
            ctypes.windll.user32.MessageBoxW(0, u"Battery low percent", u"Your battery is on low percent", 0)
            print(battery.percent)
            time.sleep(5)

