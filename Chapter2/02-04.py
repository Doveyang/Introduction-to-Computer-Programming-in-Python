# -*- coding:utf-8 -*-
d = {}
e = []
f = []
while True:
	a = raw_input("��Ŀ��\n>")
	if a != "0":
		b = raw_input("���ͣ�\n>")
		d[a] = b
	else:
		break

for i in d:
	e.append(i)
	f.append(d[i])

print e,f