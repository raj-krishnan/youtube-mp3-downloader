import time
from selenium import webdriver
from os import listdir
from os.path import isfile, join
import os

from bs4 import BeautifulSoup

def main():
    download_path = '/home/raj/Downloads/'
    firefox_profile = '/home/raj/Documents/Github/youtube-mp3-downloader/firefox_profile.default'
    profile = webdriver.FirefoxProfile(firefox_profile)
    driver = webdriver.Firefox(profile)
    choice = raw_input("Enter p for playlist download, v for individual video download: ")[0].lower()

    if choice == 'v' or choice == 'V':
        links = get_links()
        for link in links:
            download(driver, link, True)
        while 1:
            file_list = [f for f in listdir(download_path) if isfile(join(download_path,f))]
            part_files = 0
            for file in file_list:
                if file.split('.')[-1] == 'part':
                    part_files += 1
            if part_files > 0:
                time.sleep(5)
            else:
                break

    elif choice == 'p':
        playlist_url = raw_input("Enter playlist url: ")
        playlist_details = playlist_url.split("&")
        list_id = None
        for i in playlist_details:
            if "list=" in i:
                list_id = i.split("=")[1]
                break
        if list_id != None:
            download_playlist(driver, list_id)

    driver.close()

def get_links():
    link_file = open('Youtube_Links.txt', 'r')
    links = link_file.readlines()
    download_list = []
    for link in links:
        link = link.strip()
        if link != '':
            start = link.find('watch?v=') + 8
            if start != -1:
                download_list.append(link[start:])
    return download_list

def download(driver, link, youtube_dl = False):
    if not youtube_dl:
        driver.get('http://peggo.co/dvr/' + link)
        driver.find_element_by_xpath("//a[@id='record-audio']").click()
        time.sleep(20)
    else:
        os.system('youtube-dl --format bestaudio/best --extract-audio --audio-format mp3 --audio-quality 0 www.youtube.com/watch?v=' + link)

def download_playlist(driver, list_id):
    pass


if __name__ == '__main__':
    main()
