#!/usr/bin/python

import unittest, time, re
import csv
import SELENIUM_functions



def csvit(bafc,filename):

	with open(filename,'r') as c:
		x=0

			
		reader = csv.reader(c)
		for row in reader:

			if row[0] == "PRINT":
				print(row[1])

			if row[len(row)-1] == "NO":
				snap = "NO"
				x=x-1
			if row[len(row)-1] != "NO":
				snap = "YES"

			if row[0] == 'NAME':
				name = row[1]
				print ('Running the following test: ' + row[1])
				scriptname = row[1]
				bafc.append(scriptname)
				
			if row[0] != 'NAME' and row[0] != "PRINT" and row[0] != "COMMENT" and row[0] != "pause":
				x=x+1
				step = str(x).zfill(3)

			if row[0] == 'pause':
				time.sleep(5)

			if row[0] == 'openpage':
				SELENIUM_functions.open(bafc,row[1],step,snap)

			if row[0]  == "click":
				SELENIUM_functions.click(bafc,row[1],row[2],step,snap)

			if row[0] =="clickthis":
				SELENIUM_functions.clickthis(bafc,row[1],row[2],row[3],step,snap)

			if row[0]  == "entertext":
				SELENIUM_functions.entertext(bafc,row[1],row[2],row[3],step,snap)

			if row[0]  == "hover":
				SELENIUM_functions.hover(bafc,row[1],row[2],step,snap)

			if row[0] =="hoveroverthis":
				SELENIUM_functions.hoveroverthis(bafc,row[1],row[2],row[3],step,snap)

			if row[0] =="hoveroffset":
				SELENIUM_functions.hoveroverthis(bafc,row[1],row[2],row[3],row[4],step,snap)

			if row[0] =="goback":
				SELENIUM_functions.hoveroverthis(bafc,row[1],step,snap)

			if row[0] =="scroll":
				SELENIUM_functions.scroll(bafc,row[1],step,snap)



# Add custom functions below this line

