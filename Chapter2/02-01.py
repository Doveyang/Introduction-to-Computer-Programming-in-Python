# -*- coding:utf-8 -*-
a = 1
b = []
while a != 0:
	a = int(raw_input("请输入值...\n>"))
	b.append(a)

print "您输入了以下值："
print "-" * 20
i = 0
while i < len(b) - 1:
	print b[i]
	i += 1