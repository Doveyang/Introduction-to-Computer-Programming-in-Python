# -*- coding:utf-8 -*-
a = 1
b = []
while a != 0:
	a = int(raw_input("������ֵ...\n>"))
	b.append(a)

print "������������ֵ��"
print "-" * 20
i = 0
while i < len(b) - 1:
	print b[i]
	i += 1