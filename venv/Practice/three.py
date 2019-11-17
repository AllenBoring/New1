#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 21:01
# @Author  : Ryu
# @Site    : 
# @File    : three.py
# @Software: PyCharm

# 获取输入值 str1
def huiwenlian(str1):
    # 拿到输入值str1 的长度是一个int型
    str2 = len(str1)
    # 把str1 的长度减一 因为长度是从一开始的，而下表则是从0开始的所以要拿到
    # 字符串最后一个值，需要减一
    str3 = str2-1
    # 总长度除以2，是为了从中间隔开，要不然他俩轮到同一个值得时候就给判断成了是回文联
    str2 =str2 // 2
    # 先定义一个不是回文联的值，给0也就是false
    shi = 0
    # for 循环进行遍历 遍历的长度是除以2的值，因为这样的话对比到中间就结束了
    for s in range(str2):
        # 这里循环遍历的是数值，所以要用下标找到对应位置的值
        # range 方法是一个从0开始的值，所以s第一次是0 ，所显示的就是第一个值
        #  str3 则是总长度减一，就是最后一个值
        # 判断第一个值和最后一个值是否相等
        # 相等则给shi 变成1 也就是true
        # 当有不相等的时候则变成0 也就是flase
        if str1[s] == str1[str3]:
            shi = 1
            str3 -= 1
        else:
            shi = 0
    # 判断shi 是1 还是0 是1 就是回文联 是0 就不是回文联
    if shi:
        print("是")
    else:
        print("不是")


while 1:
    tey = input("请输入")
    huiwenlian(tey)
