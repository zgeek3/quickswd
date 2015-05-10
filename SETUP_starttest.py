#!/usr/bin/python

import SETUP_testsetup
import SETUP_browsersetup

def starttest():

	domain,browser,server,screenshotsdir,saucelabskey,waittime,baselinedir,savecomparisonsdir,perceptualdiff,comparefiles = SETUP_testsetup.setuptestconfigs()
	driver = SETUP_browsersetup.thebrowsersetup(browser,saucelabskey,server,domain,waittime)
	bafc = [driver,browser,server,screenshotsdir,saucelabskey,waittime,baselinedir,savecomparisonsdir,perceptualdiff,comparefiles]

	return bafc