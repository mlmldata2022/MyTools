#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''A module for converting units.'''

def temp_f2c(f):
	''' This function converts Fahrenheit to Celcius
	Input: temperature in degrees F
	Output: temperature in degrees C
	'''
	c = (f - 32.0)*(5.0/9.0)
	return(c)

def temp_c2f(c):
	''' This function converts Celcius to Fahrenheit
	Input: temperature in degrees C
	Output: temperature in degrees F
	'''
	f = c*(9/5) + 32
	return(f)

if __name__ == '__main__':
	print('do this stuff if run as script')
	print('32 degrees F:',temp_f2c(32),'C')
