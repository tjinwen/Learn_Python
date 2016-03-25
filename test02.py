#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----test02-------

print("abs(-250): ",abs(-250))
print("max(2,6,8): ",max(2,6,8))

print("int('123'): ",int('123'))
print("str(1.23): ",str(1.23))

a = abs
print("a=abs,a(-1): ",a(-1))

#-------def function------
print("---------def function------")

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >=0:
		return x
	else:
		return -x

print("def my_abs(-1): ",my_abs(-1))

def nop():
	pass

print("------------return more---------")

import math

def more(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

x,y = more(100,100,60,math.pi/6)
print("x,y = more(100,100,60,math.pi/6): ",x,y)

r = more(100,100,60,math.pi/6)
print("r = more(100,100,60,math.pi/6): ",r)

