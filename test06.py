#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#----test06-------
print("------------generator-------------")

g = (x*x for x in range(10))
for n in g:
	print(n)

print("----------------------------------")

def fib(max):
	n,a,b = 0,0,1
	while n<max:
		#print(b)
		yield b
		a,b = b,a+b
		n = n+1
	return 'done'
print(fib(6))	
#for n in fib(6):
#	print(n)
f = fib(6)
while True:
	try:
		x=next(g)
		print('g',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break
		
		
print("----------------------------------")
def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)
	
L=odd()
print(next(L))
print(next(L))
print(next(L))
