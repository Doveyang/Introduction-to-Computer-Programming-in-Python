# -*- coding:utf-8 -*-
a = raw_input("ÇëÊäÈëÒ»´®×Ö·û´®£º\n>")
length = len(a)
b = []
s = 0

for i in range(0, length):
	b.append(a[i:i + 1])

c = list(set(b))

for i in c:
	for j in b:
		if j == i:
			s +=1
	print i + "," + str(s)
	s = 0