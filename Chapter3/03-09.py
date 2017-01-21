# -*- coding:utf-8 -*-
import math
a = float(raw_input("输入系数a：\n>"))
b = float(raw_input("输入系数b：\n>"))
c = float(raw_input("输入系数c：\n>"))

delta = b * b - 4 * a * c

if delta < 0:
	print "无实数解"
elif delta == 0:
	x = (-b + math.sqrt(delta))/(2 * a)
	print "有两个相等实数解\nx = %f" % x
else:
	x1 = (-b + math.sqrt(delta))/(2 * a)
	x2 = (-b - math.sqrt(delta))/(2 * a)
	print "有两个不相等的根"
	print "X1 = %f" % x1
	print "X2 = %f" % x2