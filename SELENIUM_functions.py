#!/usr/bin/python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re
import os
import csv
import datetime
import SELENIUM_functions
import shutil
import sys
import time

# This function will open a web page.  It will replace the 'www' with the server 
# listed in the config.text file

def open(bafc,page,testname="NONE", snap="PIC"):
	driver = bafc[0]
	if testname != "NONE":
		testname = testname + "_open_"
	time.sleep(5)
	try:
		pagetoopen = page.replace("www", bafc[2])
		print("Opening: ",pagetoopen)
		driver.get(pagetoopen)

	except:
		print("Could not open " + pagetoopen)
		if snap != "NO" : snap = "FAILED"
	time.sleep(5)
	snapit(bafc,"open_",testname,snap)

# This function will click on an element on the page.

def click(bafc,thingtodo,item,testname="NONE", snap="PIC"):
	driver = bafc[0]
	if testname != "NONE":
		testname = testname + "_click_" + thingtodo + "_"

	options = ["text","partialtext","id","css","xpath","class","name","tag"]

	try:
		if thingtodo == "text":
			driver.find_element_by_link_text(item).click()			

		if thingtodo == "partialtext":
			driver.find_element_by_partial_link_text(item).click()

		if thingtodo == "id":
			driver.find_element_by_id(item).click()

		if thingtodo == "css":
			driver.find_element_by_css_selector(item).click()

		if thingtodo == "xpath":
			driver.find_element_by_xpath(item).click()

		if thingtodo == "class":
			driver.find_element_by_class_name(item).click()

		if thingtodo == "name":
			driver.find_element_by_name(item).click()

		if thingtodo == "tag":
			driver.find_element_by_tag_name(item).click()

		if thingtodo in options:
			print("Clicking ",thingtodo,":  ",item)

		if thingtodo not in options:
			print("The following option is not supported by click: ",thingtodo)
			print("Please try one of the following supported options:",options)
			snap = "FAILED"

	except:
			print("Clicking ",thingtodo,":  ",item, " failed")
			snap = "FAILED"


	snapit(bafc,"click_" + thingtodo,testname,snap)

# This function will also click on a specific element
# on a page in the case where there are multiple elements
# with the same css, xpath, etc.

def clickthis(bafc,thingtodo,item,number,testname="NONE", snap="PIC"):
	driver = bafc[0]
	if testname != "NONE":
		testname = testname + "_clickthis_" + thingtodo + "_"

	options = ["text","partialtext","id","css","xpath","class","name","tag"]


	try:
		if thingtodo == "text":
			numbers = driver.find_elements_by_link_text(item)	

		if thingtodo == "partialtext":
			numbers=driver.find_elements_by_partial_link_text(item)

		if thingtodo == "id":
			numbers=driver.find_elements_by_id(item)

		if thingtodo == "css":
			numbers=driver.find_elements_by_css_selector(item)

		if thingtodo == "xpath":
			numbers=driver.find_elements_by_xpath(item)

		if thingtodo == "class":
			numbers=driver.find_elements_by_class_name(item)

		if thingtodo == "name":
			numbers=driver.find_elements_by_name(item)

		if thingtodo == "tag":
			numbers=driver.find_elements_by_tag_name(item)

		if thingtodo in options:

			if number != "loop":
				print("Clicking ",thingtodo,":  ",item, " number:  ",number)
				i=int(number)
				numbers[i].click()
				snapit(bafc,"clickthis_" + thingtodo,testname,snap)
			if number == "loop":
				these = len(numbers)
				for i in range(0,these):
					print("Clicking ",thingtodo,":  ",item, " number:  ",i)
					numbers[i].click()
					time.sleep(5)
					snapit(bafc,"clickthis_" + thingtodo + "_" + str(i),testname,snap)

		if thingtodo not in options:
			print("The following option is not supported by click: ",thingtodo)
			print("Please try one of the following supported options:",options)
			snap = "FAILED"
			snapit(bafc,"clickthis_" + thingtodo,testname,snap)

	except:
			print("Clicking ",thingtodo,":  ",item, " failed.  Recheck the element and the index number.")
			snap = "FAILED"
			snapit(bafc,"clickthis_" + thingtodo,testname,snap)

# This function will clear text from a field and enter text to that field.

def entertext(bafc,thingtodo,item,text,testname="NONE", snap="PIC"):
	driver = bafc[0]
	if testname != "NONE":
		testname = testname + "_entertext_" + thingtodo + "_"

	options = ["id","css","xpath","class","name","tag"]
	print("This is the text:  ",text)

	if "\\n" in text:
		text = text.replace("\\n","") + "\n"


	try:

		if thingtodo == "id":
			driver.find_element_by_id(item).clear()
			driver.find_element_by_id(item).send_keys(text)

		if thingtodo == "css":
			driver.find_element_by_css_selector(item).clear()
			driver.find_element_by_css_selector(item).send_keys(text)

		if thingtodo == "xpath":
			driver.find_element_by_xpath(item).clear()
			driver.find_element_by_xpath(item).send_keys(text)

		if thingtodo == "class":
			driver.find_element_by_class_name(item).clear()
			driver.find_element_by_class_name(item).send_keys(text)

		if thingtodo == "name":
			driver.find_element_by_name(item).clear()
			driver.find_element_by_name(item).send_keys(text)

		if thingtodo == "tag":
			driver.find_element_by_tag_name(item).clear()
			driver.find_element_by_tag_name(item).send_keys(text)

		if thingtodo in options:
			print("Entering text: ",text.replace("\n"," ")," For:  ",thingtodo,":  ",item)

		if thingtodo not in options:
			print("The following option is not supported for entering text: ",thingtodo)
			print("Please try one of the following supported options:",options)
			snap = "FAILED"

	except:
			print("Entering text: ",text.replace("\n"," ")," For:  ",thingtodo,":  ",item," failed")
			snap = "FAILED"


	snapit(bafc,"entertext_" + thingtodo,testname,snap)

# This function will hover over a specific element

def hover(bafc,thingtodo,item,testname="NONE", snap="PIC"):
	driver = bafc[0]

	if testname != "NONE":
		testname = testname + "_hover_" + thingtodo + "_"

	options = ["text","partialtext","id","css","xpath","class","name","tag"]

	try:
		if thingtodo == "text":
			element_to_hover_over = driver.find_element_by_link_text(item)		

		if thingtodo == "partialtext":
			element_to_hover_over = driver.find_element_by_partial_link_text(item)

		if thingtodo == "id":
			element_to_hover_over = driver.find_element_by_id(item)

		if thingtodo == "css":
			element_to_hover_over = driver.find_element_by_css_selector(item)

		if thingtodo == "xpath":
			element_to_hover_over = driver.find_element_by_xpath(item)

		if thingtodo == "class":
			element_to_hover_over = driver.find_element_by_class_name(item)

		if thingtodo == "name":
			element_to_hover_over = driver.find_element_by_name(item)

		if thingtodo == "tag":
			element_to_hover_over = driver.find_element_by_tag_name(item)

		if thingtodo in options:
			print("Hovering over ",thingtodo,":  ",item)
			hover = ActionChains(driver).move_to_element(element_to_hover_over)
			hover.perform()	

		if thingtodo not in options:
			print("The following option is not supported by hover: ",thingtodo)
			print("Please try one of the following supported options:",options)
			snap = "FAILED"

	except:
			print("Hover over ",thingtodo,":  ",item, " failed")
			snap = "FAILED"


	snapit(bafc,"hover_" + thingtodo,testname,snap)

# This function will also hover over a specific element
# on a page in the case where there are multiple elements
# with the same css, xpath, etc.

def hoveroverthis(bafc,thingtodo,item,number,testname="NONE", snap="PIC"):
	driver = bafc[0]

	if testname != "NONE":
		testname = testname + "_hoveroverthis_" + thingtodo + "_"

	options = ["text","partialtext","id","css","xpath","class","name","tag"]


	try:
		if thingtodo == "text":
			numbers = driver.find_elements_by_link_text(item)	

		if thingtodo == "partialtext":
			numbers=driver.find_elements_by_partial_link_text(item)

		if thingtodo == "id":
			numbers=driver.find_elements_by_id(item)

		if thingtodo == "css":
			numbers=driver.find_elements_by_css_selector(item)

		if thingtodo == "xpath":
			numbers=driver.find_elements_by_xpath(item)

		if thingtodo == "class":
			numbers=driver.find_elements_by_class_name(item)

		if thingtodo == "name":
			numbers=driver.find_elements_by_name(item)

		if thingtodo == "tag":
			numbers=driver.find_elements_by_tag_name(item)

		if thingtodo in options:

			if number != "loop":
				print("Hovering over ",thingtodo,":  ",item, " number:  ",number)
				i=int(number)
				hover = ActionChains(driver).move_to_element(numbers[i])
				hover.perform()	
				snapit(bafc,"hoveroverthis_" + thingtodo,testname,snap)
			if number == "loop":
				these = len(numbers)
				for i in range(0,these):
					print("Hovering over ",thingtodo,":  ",item, " number:  ",i)
					hover = ActionChains(driver).move_to_element(numbers[i])
					hover.perform()	
					time.sleep(5)
					snapit(bafc,"hoveroverthis_" + thingtodo + "_" + str(i),testname,snap)

		if thingtodo not in options:
			print("The following option is not supported by hover over: ",thingtodo)
			print("Please try one of the following supported options:",options)
			snap = "FAILED"
			snapit(bafc,"hoveroverthis_" + thingtodo,testname,snap)

	except:
			print("Hover over ",thingtodo,":  ",item, " failed.  Recheck the element and the index number.")
			snap = "FAILED"
			snapit(bafc,"hoveroverthis_" + thingtodo,testname,snap)


# This function will go to a specific element and then hover over 
# a point based on the offset specified.

def hoveroffset(bafc,thingtodo,item,offx,offy,testname="NONE", snap="PIC"):
	driver = bafc[0]
	if testname != "NONE":
		testname = testname + "_hoveroffset_" + thingtodo + "_"

	options = ["text","partialtext","id","css","xpath","class","name","tag"]

	try:
		if thingtodo == "text":
			element_to_hover_over = driver.find_element_by_link_text(item)		

		if thingtodo == "partialtext":
			element_to_hover_over = driver.find_element_by_partial_link_text(item)

		if thingtodo == "id":
			element_to_hover_over = driver.find_element_by_id(item)

		if thingtodo == "css":
			element_to_hover_over = driver.find_element_by_css_selector(item)

		if thingtodo == "xpath":
			element_to_hover_over = driver.find_element_by_xpath(item)

		if thingtodo == "class":
			element_to_hover_over = driver.find_element_by_class_name(item)

		if thingtodo == "name":
			element_to_hover_over = driver.find_element_by_name(item)

		if thingtodo == "tag":
			element_to_hover_over = driver.find_element_by_tag_name(item)

		if thingtodo in options:
			x = int(offx)
			y = int(offy)
			print("Hovering over ",thingtodo,":  ",item, "and offsetting by x,y:  ",offx,",",offy)
			hover = ActionChains(driver).move_to_element(element_to_hover_over)
			hover = ActionChains(driver).move_by_offset(x,y)
			hover.perform()
		

		if thingtodo not in options:
			print("The following option is not supported by hover offset: ",thingtodo)
			print("Please try one of the following supported options:",options)
			snap = "FAILED"

	except:
			print("Hover offset ",thingtodo,":  ",item, " failed")
			snap = "FAILED"


	snapit(bafc,"hover_" + thingtodo,testname,snap)

# This function will navigate back using the browser back.

def goback(bafc,testname="NONE",snap="PIC"):
	driver = bafc[0]
	if testname != "NONE":
		testname = testname + "_goback_" + thingtodo + "_"
	try:
		driver.back()
		time.sleep(5)
		snapit(bafc,"goback",testname,snap)
	except:
		print("Go back failed")
		snap = "FAILED"
		snapit(bafc,"goback",testname,snap)

# This function will scroll down the page.

def scroll(bafc,scroll="1000",testname="NONE", snap="PIC"):
	driver = bafc[0]
	if testname != "NONE":
		testname = testname + "_scroll_" 

	try:
		print("Scrolling:  "  + scroll)
		c = "window.scrollTo(0," + scroll + ")"
		driver.execute_script(c)
		snapit(bafc,"scroll",testname,snap)
	except:
		print("Scroll failed")
		snap = "FAILED"
		snapit(bafc,"scroll",testname,snap)

# Custom functions begin
#         Currently there are no custom functions

# Custom functions end

# This function takes a screenshot.
	
def snapit(bafc,thingtodo,testname,snap):
	browser = bafc[1]
	trimthese = ["Firefox","IE11","LocalFirefox"]
	if testname == "NONE":
		testname = "TEST_" + (str(round(time.time()))) + "_" + thingtodo
	if snap == "NO":
		"Print -- This step does not require picture.  If you are expecting a picture please doublecheck your test."
	if snap == "PIC":
		try:
			time.sleep(5)
			bafc[0].save_screenshot(bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
			if browser in trimthese:
				os.system('convert -crop 1280x1024+0+0 ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
				print('convert -crop 1280x1024+0+0 ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
		except:
			print("Something went wrong with taking the picture of ",testname)
	if snap != "NO" and snap != "PIC" and snap != "FAILED":
		try:
			time.sleep(5)
			bafc[0].save_screenshot(bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
			if browser in trimthese:
				print('convert -crop 1280x1024+0+0 ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
				os.system('convert -crop 1280x1024+0+0 ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
		except:
			print("Something went wrong with taking the picture of name: ",testname)

	if snap == "FAILED":
		try:
			shutil.copyfile("./failure.png",bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
			shutil.copyfile("./failure.png",bafc[3] + '/' + bafc[1] + '_' + testname + '_FAILURE.png')
		except:
			print("The test failed but had a problem copying the error picture ot the right place")

	if bafc[9] == "YES" and snap != "NO": # This line was changed 4/29/2015 remove snap !="NO" if there is a problem.

		filename = bafc[1] + '_' + testname + '.png'
		perceptualdiffc = bafc[8]
		print(bafc[6] + '/' + filename)
		if os.path.exists(bafc[6] + '/' + bafc[1] + '_' + testname + '.png'):
			print("Baseline image exists:  " + bafc[6] + '/' + bafc[1] + '_' + testname + '.png')
			os.system(perceptualdiffc + ' ' + bafc[3] + '/' + filename + ' ' + bafc[6] + '/' + filename + ' -verbose -output ' + bafc[7] + '/' + filename)
			if os.path.exists(bafc[7] + '/' + filename):
				os.system('convert ' + bafc[7] + '/' + filename + ' -transparent black ' +  bafc[7] + '/' + filename)
				os.system('convert ' + bafc[7] + '/' + filename + ' -alpha set -channel a -evaluate set 50% +channel ' +  bafc[7] + '/' + filename)
				os.system('convert ' + bafc[3] + '/' + filename + ' ' + bafc[7] + '/' + filename + ' -flatten ' + bafc[7] + '/' + filename)
			if not os.path.exists(bafc[7] + '/' + filename):
				os.system('convert ' + bafc[3] + '/' + filename + ' ' + 'perfect_match.png' + ' -flatten ' + bafc[7] + '/' + filename)
		if not os.path.exists(bafc[6] + '/' + bafc[1] + '_' + testname + '.png'):
			print("Baseline image does not exist:  " + bafc[6] + '/' + bafc[1] + '_' + testname + '.png')
			os.system('convert ' + bafc[3] + '/' + filename + ' ' + 'no_baseline_available.png' + ' -flatten ' + bafc[7] + '/' + filename)

	time.sleep(1)



		









