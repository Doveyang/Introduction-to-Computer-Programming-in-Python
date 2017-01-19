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

number1 = input_dot(raw_input("请输入第一个坐标，例：(3,4)\n>"))
number2 = input_dot(raw_input("请输入第二个坐标，例：(-3,-4)\n>"))
numbers = number1 + number2
k = (float(numbers[3]) - numbers[1]) / (numbers[2] - numbers[0])
b = numbers[1] - numbers[0] * k
number3 = input_dot(raw_input("请输入第三个坐标，例：(1,1)\n>"))
distence = abs(k * number3[0] + b - number3[1]) / math.sqrt(k * k + 1)
print distence