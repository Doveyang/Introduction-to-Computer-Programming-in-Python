# -*- coding:utf-8 -*-
def judge_year(year):
	if year % 400 == 0 or year % 4 == 0:
		return 1
	else:
		return 0

list1 = [1, 3, 5, 6, 9, 11]
list2 = [4, 7, 8, 10, 12]

year = judge_year(int(raw_input('请输入年份：\n>')))
month = int(raw_input('请输入月份：\n>'))

if month == 2:
	if year:
		print "这个月有29天"
	else:
		print "这个月有28天"
elif month in list1:
	print "这个月有31天"
elif month in list2:
	print "这个月有30天"