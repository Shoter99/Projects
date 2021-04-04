from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, time

try:
    f= open("I:\Projects\PythonProjects\webScrapping\checkKeyboardPrice\data.json", "r")
    data = json.load(f)
except:
    print("Couldn't open file. \nQuiting program...")
    quit()

PATH = 'I:\Projects\PythonProjects\webScrapping\chromedriver.exe'

driver = webdriver.Chrome(PATH) 
driver.get('https://www.mediaexpert.pl/search?query%5Bmenu_item%5D=&query%5Bquerystring%5D=klawiatura%20mechaniczna&page=1&limit=30&sort=price_asc')
try:
    price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[12]/div[2]/div[3]/div[6]/div/div[2]/div[1]/div[2]/div/div/span[1]"))
    )

except :
    print("not found")
    time.sleep(3)
    driver.quit()

price = price.text
driver.quit()

if data["price"] != price:
    print("\n\nCena się zmieniła")
    if data["price"] > price:
        print(f"\nCena spadła wynosi teraz: {price} \nSprawdz: https://www.mediaexpert.pl/search?query%5Bmenu_item%5D=&query%5Bquerystring%5D=klawiatura%20mechaniczna&page=1&limit=30&sort=price_asc")

    else:
        print(f"\nCena wzrosła wynosi teraz: {price} \nSprawdz: https://www.mediaexpert.pl/search?query%5Bmenu_item%5D=&query%5Bquerystring%5D=klawiatura%20mechaniczna&page=1&limit=30&sort=price_asc")
else:
    print(f"\n\nCena się nie zmieniła")

input()