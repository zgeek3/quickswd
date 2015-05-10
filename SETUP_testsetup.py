#!/usr/bin/python

import csv

def setuptestconfigs():

	with open('config.csv','r') as c:
	
		reader = csv.reader(c)
		for row in reader:
			if row[0] == "domain":
				domain = row[1]
				print('Running in the following domain:  ',row[1])

			if row[0] == "browser":
				browser = row[1]
				print('Running in the following browser: ',row[1])
			
			if row[0] == "server":
				server = row[1]
				print('Running in the following server:  ',row[1])

			if row[0] == "screenshots":
				screenshotsdir = row[1]
				print('Screenshots will be saved in the following directory:  ',row[1])

			if row[0] == "saucelabskey":
				saucelabskey = row[1]
				print('Saucelabs key retrieved')
			if row[0] == "waittime":
				waittime = row[1]
				print('Wait time is:  ',row[1])

			if row[0] == "baselinedir":
				baselinedir = row[1]
				print('Base line directory for comparison is:  ', row[1])

			if row[0] == "savecomparisonsdir":
				savecomparisonsdir = row[1]
				print('Comparisons will be saved to the following directory: ', row[1])

			if row[0] == "perceptualdiff":
				perceptualdiff = row[1]


			if row[0] == "comparefiles":
				comparefiles = row[1]


		return domain,browser,server,screenshotsdir,saucelabskey,waittime,baselinedir,savecomparisonsdir,perceptualdiff,comparefiles

