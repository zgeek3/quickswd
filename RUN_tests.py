#!/usr/bin/python

import os
import csv
import datetime
import shutil
import sys
import time

# Number of tests to run at the same time

numteststorun = 4
teststorun = []

files = os.listdir()

for item in files:
    if item.find("TEST") != -1:
        print(item)
        teststorun.append(item)

os.system("ps -ef | grep TEST_ | awk '{print $2}' > processlist.txt")
count = sum(1 for line in open('processlist.txt'))

for test in teststorun:

    if "CSV" in test:
        os.system("python3 SETUP_any_csv.py " + test + " &")
    if "PY" in test:
        os.system("python3 " + test + " &")
    while count > (numteststorun + 1):
        time.sleep(30)
        os.system("ps -ef | grep TEST_ | awk '{print $2}' > processlist.txt")
        count = sum(1 for line in open('processlist.txt'))

count = sum(1 for line in open('processlist.txt'))

while count > 0:
    time.sleep(30)
    os.system("ps -ef | grep TEST_ | awk '{print $2}' > processlist.txt")
    count = sum(1 for line in open('processlist.txt'))

print("TESTS COMPLETED -- Now creating test reports")

print("The following number of tests failed:  )

