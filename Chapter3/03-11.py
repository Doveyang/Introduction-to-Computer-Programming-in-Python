# -*- coding:utf-8 -*-
#ð������
a =[]
while True:
	try:		
		a.append(float(raw_input("�������֣�����������ĸֵ������\n>")))
	except ValueError:
		break
		
length = len(a)
flag = True

while flag:
	flag = False
	for i in range(1,length):
		x = 0 #�����м���
		if a[i - 1] > a[i]:
			x = a[i - 1]
			a[i - 1] = a[i]
			a[i] = x
			flag = True
	length -= 1

print "���������£�"
print a