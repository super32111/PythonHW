# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = int(input("請輸入數字(邊no.1)"))
b = int(input("請輸入數字(邊no.2)"))
c = int(input("請輸入數字(邊no.3)"))

while True:
    if a+b>c and a+c>b and c+b>a:
        print("是三角形")
        break
    
    else:
        print("不是三角形")
        break
        