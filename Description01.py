#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#----Description1-------
print("**************01***************")
#######input输入的数是str类型的，int和str不能进行转换
#######type()函数可以判断数据类型	
while True:
	x=input()
	y=input()
	if(int(y)>=0 and int(y)<=10 and int(x)>=0 and int(x)<=10):
		print(int(x)+int(y))
		break