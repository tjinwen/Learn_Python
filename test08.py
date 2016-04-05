#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#----test08-------
######这个函数是个生成器，3以后的奇数，这里注意到后面的偶数不会是质数
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n

######这个函数中有lambda表达式，相当于又一个函数，筛选n的倍数		
def _not_divisible(n):
	return lambda x: x%n>0

######不断的筛选出下一个质数，it不断储存下一个奇数，这就是yield的作用，
######很方便，然后就不断筛选，it是一个数，不是list
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n=next(it)
		yield n
		it = filter(_not_divisible(n),it)
		
for n in primes():
	if n<1000:
		print(n)
	else:
		break
		
print("#############打印回数########################")

def is_palindrome(n):
	s=str(n)
	return s[::1]==s[::-1]
	
for n in range(1000,5000):
	if(is_palindrome(n)):
		print(n)
		
print("-----------------------------------")		
print(list(filter(is_palindrome,range(1,20))))