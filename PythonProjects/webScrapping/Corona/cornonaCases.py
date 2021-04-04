from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

try:
    f = open('data.json', "w")
except:
    print("Could not open file")
    quit()


PATH = 'I:\Projects\PythonProjects\webScrapping\chromedriver.exe'

driver = webdriver.Chrome(PATH) 
driver.get("https://www.worldometers.info/coronavirus/")
XPATH = '//*[@id="main_table_countries_today"]/tbody[1]/tr[20]/td[3]'

allCases = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, XPATH))).get_attribute('textContent')
todayCases = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main_table_countries_today"]/tbody[1]/tr[20]/td[4]'))).get_attribute('textContent')
yesterday = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/ul/li[2]/a[@href="#nav-yesterday"]')
driver.execute_script("arguments[0].click();", yesterday)
yesterdayCases = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div[4]/div[2]/div/table/tbody[1]/tr[20]/td[4]'))).get_attribute('textContent')
change = ""
tC = []
yC = []
if todayCases != "" and yesterdayCases != "":
	for i in todayCases:
		if i == "," or i == "+":
			continue
		else:
			tC.append(i)
	for i in yesterdayCases:
		if i == "," or i == "+":
			continue
		else:
			yC.append(i)
	sep = ""
	tC = sep.join(tC)
	yC = sep.join(yC)
	if int(tC) > int(yC):
		change = f"Liczba zakażeń wzrosła o {int(tC)-int(yC)}"
	elif int(tC) == int(yC):
		change = "Liczba zakażeń się nie zmieniła"
	else:
		change = f"Liczba zakażeń zmalała o {int(yC)-int(tC)}"
	print(change)
else:
	tC = "Nie ma danych"
	yC = "Nie ma danych"
	print(f'\n\nPrzypadki ogólnie: {allCases} \n\nPrzypadki dzisiaj: {todayCases} \n\nPrzypadki wczoraj: {yesterdayCases}\n')


json.dump(
    {"todayCases":todayCases, "allCases":allCases, "yesterdayCases":yesterdayCases}, open("data.json", "w"))

f.close()
driver.quit()
input()
