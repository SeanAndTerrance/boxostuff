#!/usr/bin/env python

#Authored by Sean and Terrance

print "Hello World, Terrance."
print "Change made by"

directory=["headquarters", "hotel", "hosptial", "house", "hotdog"]

for building in directory:
	print building

fib=[1,2]

def function_fib():
	while len(fib) < 100:
		last=fib[-1]
		second_to_last=fib[-2]
		fib.append(last+second_to_last)
	return fib

print function_fib()