from selenium import webdriver

url = 'https://www.instagram.com'

web = webdriver.Firefox(executable_path='/home/dawid/Desktop/Projects/PythonProjects/webScrap')

web.get(url)
