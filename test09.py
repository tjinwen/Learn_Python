#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#----test09-------
L=sorted([3,-1,-3,4,2,-6])
L2=sorted([3,-1,-3,4,2,-6],key=abs)

print(L)
print(L2)

print("###########homework########################")
#######这里有个好玩的地方，就是L中每个元素是（name，score）形式，
#######所以可以【0】来取第一个name
L = [('Bob', 75),('Adam', 92),('Bart', 66),('Lisa', 88)]
def by_name(t):
	return t[0].lower()
	
L2=sorted(L,key=by_name)
print(L2)

def by_score(t):
	return t[1]

L3=sorted(L,key=by_score,reverse=True)
print(L3)
