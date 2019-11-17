#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 23:46
# @Author  : Ryu
# @Site    : 
# @File    : oen.py
# @Software: PyCharm
# 猜数字小游戏
import random   # 倒入随机数包

cishu = 3 # 游戏可执行次数

zq = random.randint(1,20) # 生成一个随机数，1-20 中的 ，必须带着后面的参数，如果不带会生成的将不是数字

sr = 0       #   定义一个整形的变量放在哪里
print("请输入数字吧：")

while cishu > 0 and zq != sr :    				# 当游戏次数大于一次和输入的值不等于随机数时执行循环
	sb =input()    # 拿到输入值
	while not sb.isdigit():    					# 判断输入值是否为数字，为数字，则会返回true 不是数字返回 false
		sb = input("请输入一个数字")     		# 输入的不是数字时，让用户重新输入
	sr = int(sb)   								#　把输入的数字转换成　int　形
	cishu -= 1										#输入的次数减少一次
	if sr == zq:									#输入的值等于随机数证明猜对了
		print("真聪明，猜对了")
	else:
		if zq > sr:									#错误的话提示输入大了还是小了
			print("小了，")
		else:
			print("大了,")
		if cishu > 0:								#当次数等于０　时，游戏结束
			print("在输入一次")
		else:
			print("次数用完了")
print("游戏结束")
