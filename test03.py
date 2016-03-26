#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----test03-------

def power(x,n=2):
	s = 1
	while n>0:
		n=n-1
		s=s*x
	return s
	
def powern(x,n):
	s = 1
	while n>0:
		n=n-1
		s=s*x
	return s
	
print("power(3): ",power(3))
print("power(3,3): ",powern(3,3))

#-----------默认参数----------
print("---------------------------")

def add_end(L=[]):
	L.append('end')
	return L
print("add_end: ",add_end())
print("add_end: ",add_end())

def add_end2(L=None):
	if L is None:
		L=[]
	L.append('end')
	return L
print("add_end2: ",add_end2())
print("add_end2: ",add_end2())

#-------------------------------
print("--------------------------")

def calc(numbers):
	sum=0
	for x in numbers:
		sum=sum+x
	return sum
	
print("calc: ",calc([1,2,3,4]))

def calc2(*numbers):
	sum=0
	for x in numbers:
		sum=sum+x
	return sum
	
print("calc2: ",calc2(1,2,3))

nums = [1,2,3]
print("calc2(*nums): ",calc2(*nums))