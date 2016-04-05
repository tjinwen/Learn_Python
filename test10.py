#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#----test10-------
######丧心病狂的python的函数还能返回函数，真的不是一个具体的值，而是一个函数

def lazy_sum(*args):
	def sum():
		s=0
		for n in args:
			s=s+n
		return s
	return sum
	
#####就是这么变态，为了立即进行函数运算，可以暂时返回的是函数，强大又变态
L=lazy_sum(1,2,3,4,5)
print(L)
print(L())