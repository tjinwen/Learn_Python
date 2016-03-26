#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#----test04-------

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
	
print("递归函数fact(n): ",fact(1),fact(2),fact(5))

#print(list(range(1,100,2)))

#---------------------------
print("---------------------")

L=['tong','jin','wen']
print("L[0:2]: ",L[0:2])
print("L[1:3]: ",L[1:3])

print("abcdef[2:3]: ",'abcdef'[2:3])

