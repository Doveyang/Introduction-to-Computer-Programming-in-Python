# -*- coding:utf-8 -*-
def print_date(number):
	length = len(number)
	if length == 8:
		year = number[0:4]
		month = number[4:6]
		day = number[6:8]
		print("%s��%s��%s��") % (year, month, day)
	else:
		print "��Ч���֣�"

print_date(raw_input("������һ��8λ��\n>"))