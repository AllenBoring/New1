#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 21:20
# @Author  : Ryu
# @Site    : 
# @File    : 判断两个文件内容是否相同.py
# @Software: PyCharm



def file_open (file_1,file_2):
    differ = []
    count = 0
    for l1 in file_1:
        l2 = file_2.readline()
        count += 1
        if l1 != l2:
            differ.append(count)
    file_1.close()
    file_2.close()

    if len(differ) == 0:
        print("文件完全一样")
    else:
        print("文件共有%d处不同" % len(differ))
        for i in differ:
            print("第%d行不一样" % i)

# file_1 = open(input("请输入第一个文件"),"r")
# file_2 = open(input("请输入第二个需要比较的文件"),"r")
# file_open(file_1,file_2)

name = input("请输入第一个文件")
file_1 = open(name,"r")
nums = input("请输入行数")
print("文件%s的前%s行是：" % (name, nums))
for i in range(int(nums)):
    print(file_1.readline(),end="")