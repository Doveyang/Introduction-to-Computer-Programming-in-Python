# -*- coding:utf-8 -*-
import math
a = float(raw_input("����ϵ��a��\n>"))
b = float(raw_input("����ϵ��b��\n>"))
c = float(raw_input("����ϵ��c��\n>"))

delta = b * b - 4 * a * c

if delta < 0:
	print "��ʵ����"
elif delta == 0:
	x = (-b + math.sqrt(delta))/(2 * a)
	print "���������ʵ����\nx = %f" % x
else:
	x1 = (-b + math.sqrt(delta))/(2 * a)
	x2 = (-b - math.sqrt(delta))/(2 * a)
	print "����������ȵĸ�"
	print "X1 = %f" % x1
	print "X2 = %f" % x2