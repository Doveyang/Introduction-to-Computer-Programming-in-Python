# -*- coding:utf-8 -*-
#冒泡排序
a =[]
while True:
	try:		
		a.append(float(raw_input("输入数字（输入任意字母值结束）\n>")))
	except ValueError:
		break
		
length = len(a)
flag = True

while flag:
	flag = False
	for i in range(1,length):
		x = 0 #交换中间量
		if a[i - 1] > a[i]:
			x = a[i - 1]
			a[i - 1] = a[i]
			a[i] = x
			flag = True
	length -= 1

print "排序结果如下："
print a