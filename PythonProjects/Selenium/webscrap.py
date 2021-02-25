from selenium import webdriver;

url = 'https://www.youtube.com/channel/UCHsSYcw4HDHLy4d-dgzzxIQ'
browser = webdriver.Chrome()
browser.get(url)
text = browser.find_element_by_xpath('//*[@id="buttons"]').get_text()
print(text)
