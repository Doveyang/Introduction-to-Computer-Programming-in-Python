# -*- coding:utf-8 -*-
x = int(raw_input("输入自变量：\n>"))
if x < -5:
	y = x + 9
elif x >= 5:
	y = x + x -15
else:
	y = x * x + 2 * x + 1

print y