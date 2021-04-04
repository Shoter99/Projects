import subprocess
import re
import json

try:
    f = open('data.json', 'w')
except:
    print('Could not open file')

get_wifi = subprocess.run(
    ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

ssid_names = (re.findall("All User Profile     : (.*)\r", get_wifi))

wifi_list = list()

if len(ssid_names) != 0:
    for name in ssid_names:
        wifi_pass = dict()
        profile_info = subprocess.run(
            ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_pass["ssid"] = name
            pass_info = subprocess.run(
                ['netsh', 'wlan', 'show', 'profile', name, 'key=clear'], capture_output=True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", pass_info)
            if password == None:
                wifi_pass["password"] = None
            else:
                wifi_pass['password'] = password[1]
            wifi_list.append(wifi_pass)
json.dump(wifi_list, f)
