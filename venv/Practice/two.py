#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 22:48
# @Author  : Ryu
# @Site    : 
# @File    : two.py
# @Software: PyCharm

# c = input("请输入要打印的次数")
# i = 0
# c = int(c)
#
# while c:
#     print(i)
#     i += 1
#     c -= 1

#
# temp = input("整数")
# numb = int(temp)
# while numb :
#     i = numb-1
#     while i:
#         print(i,end="--")
#         i -= 1
#     j = numb
#     while j:
#         print(j,end="-")
#         j -= 1
#     print()
#     numb -= 1

# print(list(range(20)))
#
# c = 6
# password = "wode123"
#
# while True :
#     word = input("请输入")
#
#     if password == word :
#         print("密码正确，进入")
#         break
#     elif "%" in word:
#         print("密码中不能包含%，请重新输入,你还有",c,"次机会")
#     else:
#         c -= 1
#         print("密码错误，请重新输入,你还有",c,"次机会")
#         if c == 0:
#             print("不好意思本次服务结束")
#             break


# print("red\tyellow\tblue")
# s = 0
# for red in range (0,4):
#     for yellow in range(0,4):
#         for bule in range (2,7):
#             if red + yellow + bule == 8:
#                 s += 1
#                 print(red,'\t',yellow,'\t',bule,"第",s,"次组合")
# symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# nums = '0123456789'
#
# password = input("请输入密码")
#
# leng = len(password)
#
# while (password.isspace()) or leng == 0:
#     password = input("你输入的密码为空，请重新输入：")
#
# if leng <= 8:
#     fl = 1
# elif 8<leng<16:
#     fl = 2
# else:
#     fl = 3
# fl2 = 0
#
# for i in password:
#     if i == symbols :
#         fl2 = fl + 1
#         break
# for i in password:
#     if i == chars:
#         fl2 += 1
#         break
# for i in password:
#     if i == nums:
#         fl2 += 1
#         break
# while True:
#     print("你的密码安全级别为",end="")
#     if fl == 1 or fl2 == 1:
#         print("低")
#         break
#     elif fl == 2 or fl2 == 2:
#         print("中")
#     else:
#         print("高")
#         print("请继续保持")
#         break
# print("请按以下方式提升您的密码安全级别:,\n\
#     \t1.密码必须由数字，字母及特殊字符三种组合\n\\t2.密码只能由字母开头\n\\t3.密码长度不能低于16位")
#
# def mi(x):
#     d = x[0]
#
#     for i in x :
#         if i < d:
#             d =i
#     return d
# p=mi('032165163848646')
# print(p)

# def power (x,y):
#     q = x ** y
#     return q
#
#
#
# ss=power(4,3)
# print(ss)
def f (v):
    v = 1314
    print(v,end="")

v = 520

print(f(v))