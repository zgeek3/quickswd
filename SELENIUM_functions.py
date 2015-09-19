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

def open(bafc,page,testname="NONE", snap="PIC",teststatus="passed"):
	driver = bafc[0]
	action = "open"
	try:
		pagetoopen = page.replace("www", bafc[2])
		print("Opening: ",pagetoopen)
		driver.get(pagetoopen)

	except:
		teststatus = "failed"
	time.sleep(5)
	snapit(bafc,"open_",testname,action,snap,teststatus)

# This function will click on an element on the page.

def click(bafc,thingtodo,item,testname="NONE", snap="PIC",teststatus="passed"):
	driver = bafc[0]
	action = "click_" + thingtodo

	element = getelement(driver,thingtodo,item)[0]
	teststatus = getelement(driver,thingtodo,item)[1]

	try:
		print("Clicking ",thingtodo,":  ",item)
		element.click()
	except:
		teststatus = "failed"

	snapit(bafc,"click_" + thingtodo,testname,action,snap,teststatus)

# This function will also click on a specific element
# on a page in the case where there are multiple elements
# with the same css, xpath, etc.

def clickthis(bafc,thingtodo,item,number,testname="NONE", snap="PIC",teststatus="passed"):
	driver = bafc[0]
	action = "clickthis_" + thingtodo 

	elements = getelements(driver,thingtodo,item)[0]
	teststatus = getelements(driver,thingtodo,item)[1]

	try:
		if number != "loop":
			print("Clicking ",thingtodo,":  ",item, " number:  ",number)
			i=int(number)
			elements[i].click()
			snapit(bafc,"clickthis_" + thingtodo,testname,action,snap,teststatus)
		if number == "loop":
			these = len(elements)
			for i in range(0,these):
				print("Clicking ",thingtodo,":  ",item, " number:  ",i)
				elements[i].click()
				time.sleep(5)
				snapit(bafc,"clickthis_" + thingtodo + "_" + str(i),testname,action,snap,teststatus)
	except:
			teststatus = "failed"
			snapit(bafc,"clickthis_" + thingtodo,testname,action,snap,teststatus)

# This function will clear text from a field and enter text to that field.

def entertext(bafc,thingtodo,item,text,testname="NONE", snap="PIC",teststatus="passed"):

	driver = bafc[0]
	action = "entertext_" + thingtodo

	if "\\n" in text:
		text = text.replace("\\n","") + "\n"

	element = getelement(driver,thingtodo,item)[0]
	teststatus = getelement(driver,thingtodo,item)[1]


	try:
		print("Entering text: ",text.replace("\n"," ")," For:  ",thingtodo,":  ",item)
		element.clear()
		element.send_keys(text)

	except:
		teststatus = "failed"

	snapit(bafc,"entertext_" + thingtodo,testname,action,snap,teststatus)

# This function will hover over a specific element

def hover(bafc,thingtodo,item,testname="NONE", snap="PIC",teststatus="passed"):
	driver = bafc[0]
	action = "hover_" + thingtodo


	element = getelement(driver,thingtodo,item)[0]
	teststatus = getelement(driver,thingtodo,item)[1]

	print(element)

	try:
		print("Hovering over ",thingtodo,":  ",item)
		hover = ActionChains(driver).move_to_element(element)
		hover.perform()	

	except:
		teststatus = "failed"


	snapit(bafc,"hover_" + thingtodo,testname,action,snap,teststatus)

# This function will also hover over a specific element
# on a page in the case where there are multiple elements
# with the same css, xpath, etc.

def hoveroverthis(bafc,thingtodo,item,number,testname="NONE", snap="PIC",teststatus="passed"):
	driver = bafc[0]
	action = "hoveroverthis_" + thingtodo

	elements = getelements(driver,thingtodo,item)[0]
	teststatus = getelements(driver,thingtodo,item)[1]

	try:

		if number != "loop":
			print("Hovering over ",thingtodo,":  ",item, " number:  ",number)
			i=int(number)
			hover = ActionChains(driver).move_to_element(elements[i])
			hover.perform()	
			snapit(bafc,"hoveroverthis_" + thingtodo,testname,action,snap,teststatus)
		if number == "loop":
			these = len(elements)
			for i in range(0,these):
				print("Hovering over ",thingtodo,":  ",item, " number:  ",i)
				hover = ActionChains(driver).move_to_element(elements[i])
				hover.perform()	
				time.sleep(5)
				snapit(bafc,"hoveroverthis_" + thingtodo + "_" + str(i),testname,action,snap,teststatus)

	except:
			teststatus = "failed"
			snapit(bafc,"hoveroverthis_" + thingtodo,testname,action,snap,teststatus)


# This function will go to a specific element and then hover over 
# a point based on the offset specified.

def hoveroffset(bafc,thingtodo,item,offx,offy,testname="NONE", snap="PIC",teststatus="passed"):
	driver = bafc[0]
	action ="hoveroffset_" + thingtodo

	element = getelement(driver,thingtodo,item)[0]
	teststatus = getelement(driver,thingtodo,item)[1]


	options = ["text","partialtext","id","css","xpath","class","name","tag"]

	try:
		x = int(offx)
		y = int(offy)
		print("Hovering over ",thingtodo,":  ",item, "and offsetting by x,y:  ",offx,",",offy)
		hover = ActionChains(driver).move_to_element(element)
		hover = ActionChains(driver).move_by_offset(x,y)
		hover.perform()

	except:
		teststatus = "failed"


	snapit(bafc,"hover_" + thingtodo,testname,action,snap,teststatus)

# This function will navigate back using the browser back.

def goback(bafc,testname="NONE",snap="PIC",teststatus="passed"):
	driver = bafc[0]
	action = "goback_" + thingtodo

	try:
		driver.back()
		time.sleep(5)
		snapit(bafc,"goback",testname,action,snap,teststatus)
	except:
		teststatus = "failed"
		snapit(bafc,"goback",testname,action,snap,teststatus)

# This function will scroll down the page.

def scroll(bafc,scroll="1000",testname="NONE", snap="PIC",teststatus="passed"):
	driver = bafc[0]
	action = "scroll" 

	try:
		print("Scrolling:  "  + scroll)
		c = "window.scrollTo(0," + scroll + ")"
		driver.execute_script(c)
		snapit(bafc,"scroll",testname,action,snap,teststatus)
	except:
		teststatus = "failed"
		snapit(bafc,"scroll",testname,action,snap,teststatus)

# Custom functions begin
#         Currently there are no custom functions

# Custom functions end


# This function takes a screenshot.
	
def snapit(bafc,thingtodo,testname,action,snap,teststatus):

	browser = bafc[1]
	trimthese = ["Firefox","IE11","LocalFirefox"]
	scriptname = bafc[10]

	if testname == "NONE":
		testname = "TEST_" + (str(round(time.time()))) + action + "_" + scriptname
	if testname != "NONE":
		testname = scriptname + '_' + testname + "_" + action

	print(bafc[10] + "_" + testname + " RESULTS:  " + teststatus)

	if snap == "NO":
		"Print -- This step does not require picture.  If you are expecting a picture please doublecheck your test."
	if snap != "NO": 
		# to avoid confusion the old image and any previous failure will be removed before the new image is created
		# if snapshots are not taken then the old pictures will be left in place

		if os.path.exists(bafc[3] + '/' + bafc[1] + '_' + testname + '.png'):
			print("Deleting old screenshot")
			os.remove(bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
	
		if os.path.exists(bafc[3] + '/' + bafc[1] + '_' + testname + '_FAILURE.png'):
			print("Deleting old failure screenshot")
			os.remove(bafc[3] + '/' + bafc[1] + '_' + testname + '_FAILURE.png')

		results_directory = ["ALL","PERFECT_MATCH", "FAILURES","NO_BASELINE"]
		for result in results_directory:
			if os.path.exists(bafc[7] + '/' + result +  '/' + bafc[1] + '_' + testname + '.png'):
				print("Deleting old comparison")
				os.remove(bafc[7] + '/' + result + '/' + bafc[1] + '_' + testname + '.png')

	if snap == "PIC":
	
		try:
			time.sleep(5)
			bafc[0].save_screenshot(bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
			if browser in trimthese:
				os.system('convert -crop 1280x1024+0+0 ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
	
		except:
			print("Something went wrong with taking the picture of ",testname)
	if snap != "NO" and snap != "PIC" and teststatus != "failed":
		
		try:
			time.sleep(5)
			bafc[0].save_screenshot(bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
			if browser in trimthese:
				os.system('convert -crop 1280x1024+0+0 ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png ' + bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
		except:
			print("Something went wrong with taking the picture of name: ",testname)

	if teststatus == "failed":

		if os.path.exists(bafc[3] + '/' + bafc[1] + '_' + testname + '_FAILURE.png'):
			os.remove(bafc[3] + '/' + bafc[1] + '_' + testname + '_FAILURE.png')
		try:
			shutil.copyfile("./failure.png",bafc[3] + '/' + bafc[1] + '_' + testname + '.png')
			shutil.copyfile("./failure.png",bafc[3] + '/' + bafc[1] + '_' + testname + '_FAILURE.png')
		except:
			print("The test failed but had a problem copying the error picture to the right place")

	if bafc[9] == "YES" and snap != "NO": # This line was changed 4/29/2015 remove snap !="NO" if there is a problem.

		filename = bafc[1] + '_' + testname + '.png'
		perceptualdiffc = bafc[8]
		print(bafc[6] + '/' + filename)
		if os.path.exists(bafc[6] + '/' + bafc[1] + '_' + testname + '.png'):
			print("Baseline image exists:  " + bafc[6] + '/' + bafc[1] + '_' + testname + '.png')

			############################################################
			# Need to add check to see if images are same size otherwise there also won't be an image but not a perfect match
			############################################################

			os.system(perceptualdiffc + ' ' + bafc[3] + '/' + filename + ' ' + bafc[6] + '/' + filename + ' -verbose -output ' + bafc[7] + '/ALL/' + filename)
			print("Perceptual diff generated")
			if os.path.exists(bafc[7] + '/' + 'ALL' + '/' + filename):
				os.system('convert ' + bafc[7] + '/' + 'ALL' + '/' + filename + ' -transparent black ' +  bafc[7] + '/' + 'ALL' + '/' + filename)
				os.system('convert ' + bafc[7] + '/' + 'ALL' + '/' + filename + ' -alpha set -channel a -evaluate set 50% +channel ' +  bafc[7] + '/' + 'ALL' + '/' + filename)
				os.system('convert ' + bafc[3] + '/' + filename + ' ' + bafc[7] + '/' + 'ALL' + '/' + filename + ' -flatten ' + bafc[7] + '/' + 'ALL' + '/' + filename)
			if not os.path.exists(bafc[7] + '/' + 'ALL' + '/' + filename):
				print("The file doesn't exist so they are a perfect match")
				os.system('convert ' + bafc[3] + '/' + filename + ' ' + 'perfect_match.png' + ' -flatten ' + bafc[7]+ '/' + 'ALL' + '/' + filename)
				shutil.copyfile(bafc[7]+ '/' + 'ALL' + '/' + filename,bafc[7]+ '/' + 'PERFECT_MATCH' + '/' + filename)
			if teststatus == "failed":
				shutil.copyfile(bafc[7]+ '/' + 'ALL' + '/' + filename,bafc[7]+ '/' + 'FAILURES' + '/' + filename)
		if not os.path.exists(bafc[6] + '/' + bafc[1] + '_' + testname + '.png'):
			print("Baseline image does not exist:  " + bafc[6] + '/' + bafc[1] + '_' + testname + '.png')
			os.system('convert ' + bafc[3] + '/' + filename + ' ' + 'no_baseline_available.png' + ' -flatten ' + bafc[7] + '/' + 'ALL' + '/' + filename)
			shutil.copyfile(bafc[7]+ '/' + 'ALL' + '/' + filename,bafc[7]+ '/' + 'NO_BASELINE' + '/' + filename)

	time.sleep(1)

# This function will get an element and return an error if element is not available.

def getelement(driver,thingtodo,item,teststatus="passed"):
	
	options = ["text","partialtext","id","css","xpath","class","name","tag"]
	try:

		if thingtodo == "text":
			element = driver.find_element_by_link_text(item)		

		if thingtodo == "partialtext":
			element = driver.find_element_by_partial_link_text(item)

		if thingtodo == "id":
			element = driver.find_element_by_id(item)

		if thingtodo == "css":
			element = driver.find_element_by_css_selector(item)

		if thingtodo == "xpath":
			element = driver.find_element_by_xpath(item)

		if thingtodo == "class":
			element = driver.find_element_by_class_name(item)

		if thingtodo == "name":
			element = driver.find_element_by_name(item)

		if thingtodo == "tag":
			element = driver.find_element_by_tag_name(item)

		if thingtodo not in options:
			print("The following option is not supported by click: ",thingtodo)
			print("Please try one of the following supported options:",options)
			element = "ERROR"
			teststatus = "failed"
	except:
		element = "ERROR"
		teststatus = "failed"

	return element,teststatus

# This function will get a set of elements and return an error if the elements are not available.

def getelements(driver,thingtodo,item,teststatus="passed"):

	options = ["text","partialtext","id","css","xpath","class","name","tag"]
	try:

		if thingtodo == "text":
			elements = driver.find_elements_by_link_text(item)	

		if thingtodo == "partialtext":
			elements=driver.find_elements_by_partial_link_text(item)

		if thingtodo == "id":
			elements=driver.find_elements_by_id(item)

		if thingtodo == "css":
			elements=driver.find_elements_by_css_selector(item)

		if thingtodo == "xpath":
			elements=driver.find_elements_by_xpath(item)

		if thingtodo == "class":
			elements=driver.find_elements_by_class_name(item)

		if thingtodo == "name":
			elements=driver.find_elements_by_name(item)

		if thingtodo == "tag":
			elements=driver.find_elements_by_tag_name(item)

		if thingtodo not in options:
			print("The following option is not supported by click: ",thingtodo)
			print("Please try one of the following supported options:",options)
			elements = "ERROR"
			teststatus = "failed"
	except:
		element = "ERROR"
		teststatus = "failed"

	return elements,teststatus



		









