# -*- coding:utf-8 -*-
import math

def input_dot(dot):
	element = []
	part = dot.split(',')
	part1 = part[0].strip()
	part2 = part[1].strip()
	x = int(part1.strip('('))
	y = int(part2.strip(')'))
	element.append(x)
	element.append(y)
	return element

number1 = input_dot(raw_input("请输入一个第一象限的坐标，例：(3,4)\n>"))
number2 = input_dot(raw_input("请输入一个第三象限的坐标，例：(-3,-4)\n>"))
numbers = number1 + number2
a = numbers[0]
b = numbers[1]
c = numbers[2]
d = numbers[3]

distence = math.sqrt((a - b) * (a - b) + (c - d) * (c - d))
print distence