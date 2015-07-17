#!/usr/bin/python

import SELENIUM_functions
import SETUP_starttest
import unittest, time, re

bafc = SETUP_starttest.starttest()
driver = bafc[0]

scriptname = "Example_python_test"
print("Running test:  " + scriptname)

bafc.append(scriptname)

SELENIUM_functions.open(bafc,"https://www.google.com/","1_google")
SELENIUM_functions.entertext(bafc,"id","lst-ib","selenium webdriver \n","2_search_term")
SELENIUM_functions.click(bafc,"text","Selenium - Web Browser Automation","3_go_to_selenium")
SELENIUM_functions.clickthis(bafc,"css","div#header > ul > li","0","4_about")
SELENIUM_functions.hover(bafc,"text","License","5_license")
SELENIUM_functions.click(bafc,"text","Licens","6_license") #intentional misspelling to demonstrate failure case

time.sleep(5)

driver.quit()
