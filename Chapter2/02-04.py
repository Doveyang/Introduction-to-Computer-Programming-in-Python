# -*- coding:utf-8 -*-
d = {}
e = []
f = []
while True:
	a = raw_input("ÏîÄ¿£º\n>")
	if a != "0":
		b = raw_input("½âÊÍ£º\n>")
		d[a] = b
	else:
		break

for i in d:
	e.append(i)
	f.append(d[i])

print e,f