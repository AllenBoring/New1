#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 22:49
# @Author  : Ryu
# @Site    : 
# @File    : 递归.py
# @Software: PyCharm
# 普通函数
from fractions import _gcd

def reset(s):
    b = 1
    for i in range(s):
        i += 1
        b = i * b
    return b
# 递归函数，递归就是函数自己调用自己
def res (n):
    if n == 1:
        return 1
    else:
        return n * res(n-1)
print(reset(5))
print(res(5))
# 递归的方法写的X的Y次幂
def g(x,y):
    if x ==0:
        return 0
    elif y==0:
        return 1
    else:
        return g(x,y-1)*x
print(g(2,4))


# 非递归实现   最大公约数
def gcd_test_one(a, b):
    if a != 0 and b != 0:
        if a > b:
            a, b = b, a
        if b % a == 0:
            return a
        gcd_list = []
        for i in range(1, a):
            if b % i == 0 and a % i == 0:
                gcd_list.append(i)
        return max(gcd_list)
    else:
        print
        'Number is wrong!!!'


# 递归实现    最大公约数
def gcd_test_two(a, b):
    if a > b:
        a, b = b, a
    if b % a == 0:
        return a
    else:
        return gcd_test_two(a, b % a)


# python自带的gcd
def gcd_test_three(a, b):
    return _gcd(a, b)


