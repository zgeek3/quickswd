#!/usr/bin/python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 

def thebrowsersetup(browser,saucelabskey,server,domain,waittime):


	if browser == "Chrome":
		try:

			driver = webdriver.Chrome()
			driver.implicitly_wait(waittime)
			driver.set_window_size(1280,1024)
			driver.get("http://" + server + '.' + domain)
			return driver
		except:
			print("Could not setup the test for:  ",browser)
			print("Something happened opening the browser")

	if browser == "LocalFirefox":
		try:

			driver = webdriver.Firefox()
			driver.implicitly_wait(waittime)
			driver.set_window_size(1280,1024)
			driver.get("http://" + server + '.' + domain)
			return driver
		except:
			print("Could not setup the test for:  ",browser)
			print("Something happened opening the browser")

	if browser == "SauceChrome":
		try:
			caps = {'browserName': "chrome"}
			caps['platform'] = "Windows 8.1"
			caps['version'] = "41.0"
			caps['screenResolution'] = "1280x1024"
			caps['record-video'] = "false"
			caps['record-screenshots'] = "false"

			driver = webdriver.Remote(desired_capabilities=caps,command_executor=saucelabskey)
			driver.implicitly_wait(waittime)

			driver.set_window_size(1280,1024)

			print('Currently testing Chrome on Saucelabs')

			driver.get("http://" + server + '.' + domain)
			return driver
		except:
			print("Could not setup the test for:  ",browser)
			print("Something happened with saucelabs or opening the browser")

	if browser == "Firefox":
		try:
		# Firefox test
			caps = webdriver.DesiredCapabilities.FIREFOX
			caps['platform'] = "Windows 8.1"
			caps['version'] = "37.0"
			caps['screenResolution'] = "1280x1024"
			caps['record-video'] = "false"
			caps['record-screenshots'] = "false"

			driver = webdriver.Remote(desired_capabilities=caps,command_executor=saucelabskey)
			driver.implicitly_wait(waittime)

			driver.set_window_size(1280,1024)

			print('Currently testing FIREFOX')

			driver.get("http://" + server + '.' + domain)
			return driver
		except:
			print("Could not setup the test for:  ",browser)
			print("Something happened with saucelabs or opening the browser")


	if browser == "Safari":
		try:

			# Safari test

			caps = webdriver.DesiredCapabilities.SAFARI
			caps['platform'] = "OS X 10.10"
			caps['version'] = "8.0"
			caps['screen-resolution'] = "1280x1024"
			caps['record-video'] = "false"
			caps['record-screenshots'] = "false"

			driver = webdriver.Remote(desired_capabilities=caps,command_executor=saucelabskey)
			driver.implicitly_wait(waititme)

			print('Currently testing Safari')

			driver.get("http://" + server + '.' + domain)
			return driver
		except:
			print("Could not setup the test for:  ",browser)
			print("Something happened with saucelabs or opening the browser")

	if browser == "IE11":
		try:

		# IE 11 test

			caps = webdriver.DesiredCapabilities.INTERNETEXPLORER
			caps['platform'] = "Windows 8.1"
			caps['version'] = "11"
			caps['screen-resolution'] = "1280x1024"
			caps['record-video'] = "false"
			caps['record-screenshots'] = "false"

			driver = webdriver.Remote(desired_capabilities=caps,command_executor=saucelabskey)
			driver.implicitly_wait(waittime)
			driver.set_window_size(1280,1024)

			print('Currently testing IE 11')
			
			driver.get("http://" + server + '.' + domain)
			return driver
		except:
			print("Could not setup the test for:  ",browser)
			print("Something happened with saucelabs or opening the browser")
