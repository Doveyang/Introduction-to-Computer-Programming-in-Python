# -*- coding:utf-8 -*-
list = ['甲', '乙', '丙', '丁', '戊']
name = raw_input("请输入学生姓名:\n>")
if name in list:
	print "找到此人"
else:
	print "查无此人"