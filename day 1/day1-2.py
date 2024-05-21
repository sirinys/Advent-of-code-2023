# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:43:19 2023

@author: Siri
"""
sum = 0

digits_text = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


digits_map = {digits_text[i]: i for i in range(len(digits_text))}

def getfirstnum(line):
    i = 0
    while i <= len(line):
        digits = list(filter(str.isdigit, line[:i]))
        if len(digits) > 0:
            return digits[0]
        for text, num in digits_map.items():
            if (line[:i].find(text) != -1):
                return num
        i += 1
        
def getlastnum(line):
    i = len(line)-1
    while i >= 0:
        digits = list(filter(str.isdigit, line[i:]))
        if len(digits) > 0:
            return digits[0]
        for text, num in digits_map.items():
            if (line[i:].find(text) != -1):
                return num
        i -= 1
    

with open("input_dag1-1.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    firstNum = getfirstnum(line)
    lastNum = getlastnum(line)
    sum += (int(firstNum)*10 + int(lastNum))
        
print("\n" + str(sum))