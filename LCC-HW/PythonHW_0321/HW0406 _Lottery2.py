# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:16:16 2023

@author: User
"""

import random

min = 1
max = 49

num = []
while len(num) < 6:
    n = int(input("請輸入6個號碼(1-49):"))
    if num.count(n) == 0:
        num.append(n)
    else:
        print("請重新輸入6個號碼(1-49)")
print(num)

m = []
for i in range(6):
    ram = random.randint(min, max)
    m.append(ram)
print(m)






