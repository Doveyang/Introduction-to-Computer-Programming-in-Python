# -*- coding:utf-8 -*-
year = int(raw_input('��������ݣ�\n>'))
if year % 400 == 0 or year % 4 == 0:
	print "����"
else:
	print "��������"
