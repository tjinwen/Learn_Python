names = ['Micheal','Bob','Tracy']
for name in names:
	print(name)
	
#-----------------------
sum = 0
for x in range(101):
	sum = sum + x
print(sum)

#------------------------
#peplo = ['tong','jin','wen']
#scores = [95,75,85]

NameS = {'tong':95,'jin':93,'wen':45}
print(NameS['tong'])

#--------learn set----------
print("-------------------")
s = set([1,2,3,2,3])
print(s)

s.add(4)
print(s)

s.remove(3)
print(s)

print("----set 可以做数学上的一些集合的运算----")
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1&s2)
print(s1|s2)


