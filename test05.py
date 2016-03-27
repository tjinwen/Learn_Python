#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#----test05-------

L=[]
for x in range(1,11):
	L.append(x*x)
print(L)

L2=[x*x for x in range(1,11)]
print(L2)

print("------------------------")
print("m+n for m in 'abc' for n in 'xyz':")
print([m+n for m in 'abc' for n in 'xyz'])

print("------------------------")
L3={'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in L3.items()])

print("------------------------")
L4=['Hello','World',18,'Apple',None]
L5=[]
for n in L4:
	if isinstance(n,str):
		L5.append(n.lower())
	#else:
	#	L5.append(n)
print(L5)