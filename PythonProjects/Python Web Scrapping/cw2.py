import requests as r

url = 'https://en.wikipedia.org'

re = r.get(url, allow_redirects=True)
open('robot.txt', 'wb').write(re.content)
