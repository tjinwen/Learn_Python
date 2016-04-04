#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#----test06-------
def add(x,y,f):
	return f(x)+f(y)
print(add(-1,-2,abs))

print('--------------------------')
def fx(x):
	return x*x

r = map(fx,[1,2,3,4,5,6,7])
print(list(r))

print()
print('----------------------------')

from functools import reduce
def fn(x,y):
	return x*10+y

a = reduce(fn,[1,2,3,4])
print("like fn(fn(fn(1,2),3),4): ")
print(a)

print()
print('----------------------------')
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	
b = reduce(fn,map(char2num,'13579'))
print(b)
print(list(map(char2num,'13579')))