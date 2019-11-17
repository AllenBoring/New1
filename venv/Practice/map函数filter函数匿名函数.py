#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 21:25
# @Author  : Ryu
# @Site    : 
# @File    : map函数filter函数匿名函数.py
# @Software: PyCharm

# 普通函数
def my(x):
    return  x % 3==0

# 匿名函数
lambda  x,y :x * y

# filter 过滤器，第一个是函数第二个是序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# 一、函数：不带括号时，调用的是这个函数本身 ，是整个函数体，是一个函数对象，不须等该函数执行完成
# 二、函数：带括号（参数或者无参），调用的是函数的执行结果，须等该函数执行完成的结果
w=list(filter(lambda x:(x%2),range(20)))
print(w)
#函数不带括号才可以调用
s=list(filter(my,range(20)))
print(s)
#带括号调用会报错,提示bool”对象不可调用
# q= 100
# q=list(filter(my(q),range(q)))
# print(q)

# map函数,第一个和filter 函数一样都是要传一个函数进去，前面是函数执行方法，后面是函数执行的参数
# 第二个是多个一个或多个序列
# 前面是一个平方计算，后面是一个从0 到19的集合
te = map(lambda n : n ** 2 ,range(20))
print(list(te))
# 这个是函数计算有问题后面给了两个参数，而函数只能接收一个，所以会报错
# te1 = map(lambda n : n ** 2 ,[3,63.5,85],[2,5,6.2])
# print(list(te1))

te1 = map(lambda n,x :[n,x],range(8),range(10))
print(list(te1))

# 函数方法，
def my1(x,w):
    return x,w
list1 = list(range(9))
list2 = list(range(7))
# map函数会自动取到小可执行参数
print(list(map(my1,list2,list1)))

def make(x):
    return lambda s : s+x
    # x=x+1
    # def d(s):
    #     s = s + x
    #     return s
    # return s

# 外函数的返回值是内函数的名称
def mkae1(x):
    def make2(y):
        y = x*y
        return y
    return make2
# 调用外函数赋值给double 然后double就可以调用内函数了
double = mkae1(3)
print(double(9))