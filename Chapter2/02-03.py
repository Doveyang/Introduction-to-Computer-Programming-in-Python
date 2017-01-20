# -*- coding:utf-8 -*-
a = 1
b = []
while a != 0:
	c = raw_input("ÇëÊäÈëÖµ...\n>")
	a = int(c)
	b.append(c)
	if a == 0:
		b.remove("0")
		
t = tuple(b)
print t