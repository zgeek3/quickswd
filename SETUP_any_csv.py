#!/usr/bin/python

import SETUP_starttest
import SETUP_csv
import sys

bafc = SETUP_starttest.starttest()
driver = bafc[0]

for arg in sys.argv:
	print (arg)

SETUP_csv.csvit(bafc,sys.argv[1])

driver.quit()

