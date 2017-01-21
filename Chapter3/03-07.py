# -*- coding:utf-8 -*-
year = int(raw_input('请输入年份：\n>'))
if year % 400 == 0 or year % 4 == 0:
	print "闰年"
else:
	print "不是闰年"
