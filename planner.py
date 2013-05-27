#!/usr/bin/env python

import sys
import os.path
import os

# def main ():
# 	print "Welcome"
# 	print "1 - Add Event"
# 	print "2 - Search for Event"
# 	print "3 - Remove Event"
# 	print "4 - Exit Program"
planner={}

def addEvent(planner):
	time = raw_input ("Please select a time for this event: ")
	event = raw_input ("Select event to occur at this time: ")
	planner[time]= event
	return planner

def write():
	if os.path.exists('plans.txt') == True:
		varWriteOut = open('plans.txt', "a")
		varWriteOut.write('%s\n' % (planner))
		varWriteOut.close()
	else:
		varWriteOut = open('plans.txt', "w")
		varWriteOut.write('%s\n' % (planner))
		varWriteOut.close()


while True:
	placeholdervariable = raw_input("Enter 1-4 or fuck off: ")

	if placeholdervariable == "1":
		sys.exit()
	elif placeholdervariable == "2":
		addEvent(planner)
		print planner
		write()
	elif placeholdervariable == "3":
		funcanotherplaceholderfuck()
	else:
		print "Please enter a valid option."
		continue

