#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 22:42
# @Author  : Ryu
# @Site    : 
# @File    : five闭包的调用.py
# @Software: PyCharm

# 外函数
def my1():
    s = 5
    print(s,"次")
    # 内函数
    def my2 ():
        nonlocal s
        s += 1
        print("这就是我第 %d 次打印"%(s))
    #     返回的是一个名字，这个名字是指向值
    return  my2

def my3():
    j = 0
    print(j,"次")
    def my4 ():
        nonlocal j
        j += 1
        print("这就是我第 %d 次打印"%(j))
    return  my4()

# 这个是执行外函数，一次，并且把内嵌函数指向了一个名字,
# 也可以算是初始化内函数,只要q 没有被重新赋值my1（）就没有被释放
# 也就是说局部变量 没有被重新初始化
q = my1()
print("tttttttttttttt----------------------------------------")
t = 3
while t :
    t -= 1
    # 这样无法调用函数
    my3
print("iiiiiiiiii----------------------------------------")

i=3
while i :
    i = i-1
    # 这个是从头开始执行函数，同时执行外函数和内函数
    my1()()
print("ooooo----------------------------------------")

o = 3
while o:
    o -= 1
    # 调用函数，从外函数开始执行
    my3()
print("uuuuuu----------------------------------------")
u = 3
while u:
    u -= 1
    # 这个是只执行内函数，并且不清空上一次的值，例如
    # 上一次执行完s = 6 ，下一次进行加一的话就是用 6+1来执行的
    q()




