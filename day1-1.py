# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:46:06 2023

@author: Siri
"""

sum = 0

with open("input_dag1-1.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    nums = list(filter(str.isdigit, line))
    sum += (int(nums[0])*10 + int(nums[-1]))
    
print(sum)