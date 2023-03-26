# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 01:36:33 2023

@author: User
"""



while True:
    a = int(input("請輸入大於0的數字(邊no.1)"))
    b = int(input("請輸入大於0的數字((邊no.2)"))
    c = int(input("請輸入大於0的數字((邊no.3)"))
    
    if a+b<=c or a+c<=b or c+b<=a:
        print("不是三角形")
        
    elif a+b>c and a+c>b and c+b>a and a==b==c:
        print("正三角形")
        break
    
    elif a+b>c and a+c>b and c+b>a and a==b or a==c or b==c:
        print("等腰三角形")
        break
        
    else:
        print("三角形")
        break
        