#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#----test06-------
def add(x,y,f):
	return f(x)+f(y)
print(add(-1,-2,abs))