#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 21:49
# @Author  : Ryu
# @Site    : 
# @File    : four（计算字符串参数）.py
# @Software: PyCharm

def my(*diy):
    le = len(diy)
    for i in range(le):
        zimu = 0
        kongge = 0
        shuzi = 0
        qita = 0
        for s in diy[i]:
            if s.isdigit():
                shuzi += 1
            elif s.isalnum():
                zimu += 1
            elif s == " ":
                kongge +=1
            else:
                qita +=1

        print(shuzi,"个数字",zimu,"个字母",kongge,"个空格",qita,"个其他")


input("请输入字符串")
my("dsada212ddada ada ","dsad5a1d3a,da")