#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 19:23
# @Author  : Ryu
# @Site    : 
# @File    : 创建文件.py
# @Software: PyCharm

# def get_doc (file_name):
#     d = docx.opendocx(file_name)
#     doc = docx.getdocumenttext(d)
#     return doc

# doc = get_doc(r'C:\Users\ASUS--\Desktop\对话解释.docx')
# print(doc)

# file = open(r'C:\Users\ASUS--\Desktop\对话解释1.txt',encoding='UTF-8')
# file.readlin    只读取一行
# flie.readlins    读取每一行
# filr.read      读取所有
#  可以不用转换list 直接进行for循环遍历，这样比较省内存
# 文件读取后，指针指向最后位置，再次读取则没有内容
# for o in file:
#     print("===========",o)
#指针重新指向开始的位置才能再次读取到文件内容
# file.seek(0)
# list1= list(file.readlines())
# for i in list1:
#     print(i)
# file.write("第一次插入内容")
#文件只有关闭后，所写入的内容才能保存在text 文本中
# file.close()

def create_file(c,b):
    flie_name = '第' + str(c) + '个' + '.txt'
    name = open(flie_name, 'w', encoding='utf-8')
    name.writelines(b)
    name.close()

file = open(r"C:\Users\ASUS--\Desktop\对话解释1.txt",encoding="utf-8")

boy1 = []
girl = []
count = 1

for each_g in file:
    if each_g[:5] != "....." :
        boy1.append(each_g)
    else:
      create_file(count,boy1)
      boy1 = []
      count = count + 1
create_file(count,boy1)
file.close()
