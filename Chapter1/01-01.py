# -*- coding:utf-8 -*-
def print_date(number):
	length = len(number)
	if length == 8:
		year = number[0:4]
		month = number[4:6]
		day = number[6:8]
		print("%s年%s月%s日") % (year, month, day)
	else:
		print "无效数字！"

print_date(raw_input("请输入一个8位数\n>"))