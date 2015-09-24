import time
from selenium import webdriver
from os import listdir
from os.path import isfile, join

def main():
	download_path = '/home/raj/Downloads/'
	links = get_links()
	profile = webdriver.FirefoxProfile()

	profile.set_preference('browser.download.folderList', 2)
	profile.set_preference('browser.download.manager.showWhenStarting', False)
	profile.set_preference('browser.download.dir', download_path)
	profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'audio/mpeg')

	driver = webdriver.Firefox(profile)

	for link in links:
		download(driver, link)

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

def download(driver, link):
	driver.get('http://peggo.co/dvr/' + link)
	driver.find_element_by_xpath("//a[@id='record-audio']").click()
	time.sleep(30)

if __name__ == '__main__':
	main()
