from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from scripts.links import Link
from scripts.download import Downloader

if __name__ == '__main__':
    try:
        numOfSongs = int(input("Podaj ilosc piosenek w playliscie: "))
        linkToPlaylist = input('Podaj link do playlisty: ')
    except Exception as e:
        print("Zla liczba")
        quit()
    try:
        driver = webdriver.Chrome()
        driver.get(
            linkToPlaylist)
    except Exception as e:
        print("Nie ma takiej playlisty lub sterownik nie działa")
    acc = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button')
    acc.click()

    link = Link(driver)
    downloader = Downloader(driver)
    links = link.saveLinks(numOfSongs)
    for link in links:
        downloader.openSite()
        downloader.DownloadItem(link)
    driver.close()
