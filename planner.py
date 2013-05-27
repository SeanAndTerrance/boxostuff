#!/usr/bin/env python

# def main ():
# 	print "Welcome"
# 	print "1 - Add Event"
# 	print "2 - Search for Event"
# 	print "3 - Remove Event"
# 	print "4 - Exit Program"
planner={}

def addEvent(planner):
	time = raw_input ("Please select a time for this event")
	event = raw_input ("Select event to occur at this time")
	planner[time]= event
	return planner


while True:
	placeholdervariable = raw_input("Enter 1-4 or fuck off")

	if placeholdervariable == "1":
		sys.exit()
	elif placeholdervariable == "2":
		addEvent(planner)
		print planner
	elif placeholdervariable == "3":
		funcanotherplaceholderfuck()
	else:
		print "Please enter a valid option."
		continue

