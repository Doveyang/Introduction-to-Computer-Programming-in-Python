# -*- coding:utf-8 -*-
a = raw_input("请输入一个小数...\n>")
b = []
b = a.split('.')
z = b[0]
x = b[1]
x1 = int(x[0:1])
x2 = int(x[1:2])
x3 = int(x[2:3])

if x3 >= 5:
	x2 += 1

number = int(z) + x1 * 0.1 + x2 * 0.01

print str(number) 