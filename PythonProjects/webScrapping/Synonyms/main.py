from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'I:\Projects\PythonProjects\webScrapping\chromedriver.exe'

search = input("Do jakiego wyrazu szukasz synonimów: ")
driver = webdriver.Chrome(PATH)
driver.get(f'https://www.synonimy.pl/synonim/{search}/')

try:
    synonym = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "word_load"))
    )
except :
    print("Nie znaleziono takiego słowa")
    time.sleep(4)
    driver.quit()

print(f"{synonym.text}")
driver.quit()
input()