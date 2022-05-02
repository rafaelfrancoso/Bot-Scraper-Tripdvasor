import sys
import csv
from selenium import webdriver
import time

path_to_file = "restaurants.csv"


#num_page = 163
num_page = 19
listUrl = []
listRegions = []


url = "https://www.tripadvisor.cl/Restaurants-g294291-Chile.html"

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get(url)


csvFile = open(path_to_file, 'a', encoding="utf-8", newline='')
csvWriter = csv.writer(csvFile, delimiter=';')


#container = driver.find_elements_by_xpath('//*[@class="OhCyu"]/span/a')
#time.sleep(2)


container = driver.find_elements_by_xpath('//*[@class="geo_name"]/a')
time.sleep(2)
cookie = driver.find_element_by_id('onetrust-accept-btn-handler').click()
for city in range(len(container)):
    listRegions.append(container[city].get_attribute('href'))
time.sleep(1)
driver.get("https://www.tripadvisor.cl/Restaurants-g294291-oa20-Chile.html")
    

for i in range(0, num_page):
    time.sleep(2)
    container = driver.find_elements_by_xpath('//*[@class="geoList"]/li/a')
    for city2 in range(len(container)):
    	listRegions.append(container[city2].get_attribute('href'))
    time.sleep(1)
    try:
    	button = driver.find_element_by_xpath('//*[@class="guiArw sprite-pageNext  pid0"]').click()
    except:
    	button=""


for regions in listRegions:
	driver.get(regions)
	#for i in range(0, max_page):
	while True:
		time.sleep(3)
		container = driver.find_elements_by_xpath('//*[@class="OhCyu"]/span/a')
		for link in range(len(container)):
			listUrl.append(container[link].get_attribute('href'))
		time.sleep(2)
		try:
			button = driver.find_element_by_xpath('//*[@class="nav next rndBtn ui_button primary taLnk"]').click()
		except:
			break


#for link in range(len(container)):
	#listUrl.append(container[link].get_attribute('href'))
	


for link2 in listUrl:
	time.sleep(2)
	driver.get(link2)                    
	try:
		name = driver.find_element_by_tag_name('h1').text
	except:
		name = ""
	try:
		regionC = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[5]/div/div/div/div[2]/ul/li[4]/a/span").text
	except:
		regionC = ""
	try:
		number = driver.find_element_by_xpath('//a[@class="fhGHT"]/span/b').text
	except:
		number = ""
	try:
		typeR = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/div/div/div[2]/span[3]/a[1]").text
	except:
		typeR = ""
	try:
		typeR2 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/div/div/div[2]/span[3]/a[2]').text
	except:
		typeR2 = ""
	try:
		typeR3 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/div/div/div[2]/span[3]/a[3]').text
	except:
		typeR3 = ""
	try:
		typeR4 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/div/div/div[2]/span[3]/a[4]').text
	except:
		typeR4 = "-"
	try:
		telephone = driver.find_element_by_xpath('//*[@class="fhGHT"]/a').get_attribute('href')
		telephone = telephone.replace("tel:","")
	except:
		telephone = ""
	try:
		site = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[1]/span/a').get_attribute('href')
	except:
		site = ""
	try:
		email = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[2]/span/a').get_attribute('href')
		email = email.replace("mailto:","").replace("?subject=?","")
	except:
		email = "-"
	try:
		menu = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[3]/span[4]/a').get_attribute('href')
	except:
		menu = "-"
	try:
		typeF = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]').text
	except:
		typeF = "-"
	try:
		localization = driver.find_element_by_xpath('//*[@class="brMTW"]').text
	except:
		localization = "-"

	dados = [name, regionC, number, typeR, typeR2, typeR3, typeR4, telephone, site, email, menu, typeF, localization]
	print(dados)

	csvWriter.writerow(dados)
	csvFile.flush()


driver.quit()




