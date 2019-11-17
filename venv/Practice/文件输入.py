#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 21:26
# @Author  : Ryu
# @Site    : 
# @File    : 文件输入.py
# @Software: PyCharm

name_1 = []
name_2 = r"C:\Users\ASUS--\Desktop\我的文件\\"
txt_1 = []
txt_2 = []

name_1 = input("请输入文件名")
txt_1 = input("请输入内容【单独输入：“w”保存退出】")
while txt_1 != 'w':
    txt_2.append(txt_1+'\n')
    txt_1=input()

name_1 =name_2 + name_1 + ".txt"
file_txt = open(name_1,'w')
file_txt.writelines(txt_2)
file_txt.close()