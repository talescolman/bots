# pip install selenium

from selenium import webdriver # open the browser from your code
from time import sleep

# download a  driver from chromedriver.storage.googleapis.com/

driver = webdriver.Chrome(executable_path="/Users/downloads/mydriver") # use the path where you stored your driver

# load the instagram page
driver.get("https://instagram.com")
sleep(5) # time it takes to open the instagram page

# log in on Instagram
driver.find_element_by_xpath(("//input[@name=\"username\"]"))
	.send_keys(("put your username here!"))
driver.find_element_by_xpath(("//input[@name=\"password\"]"))
	.send_keys(("put your password here!"))
# submit
driver.find_element_by_xpath(('/button[@type="submit"]'))
	.click()
sleep(4) # time to load the page

# eliminate the notifications box
driver.find_element_by_xpath("//button[contains(text()), 'Not Now')]")\
	.click()

# loop for how many times it will happen
for i in range(3):
# crate a loop that will follow the suggestion box
	for i in range(5): # 5 because there are 5 follow suggestions on the page
		driver.find_element_by_xpath('//button[text()="Follow"]')\
			.click()
		sleep(3)
	driver.refresh() # to reload the page after a while
