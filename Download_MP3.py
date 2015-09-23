import time
from selenium import webdriver

def download(driver, link):
	driver.get('http://peggo.co/dvr/' + link)
	driver.find_element_by_xpath("//a[@id='record-audio']").click()
	time.sleep(30)

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

def main():
	links = get_links()
	driver = webdriver.Firefox()
	for link in links:
		download(driver, link)

	input = raw_input('Enter Y when downloads are complete: ')
	while input != "Y":
		input = raw_input('Enter Y when downloads are complete: ')

	driver.close()

if __name__ == '__main__':
	main()
