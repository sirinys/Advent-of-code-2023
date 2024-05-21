# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:43:19 2023

@author: Siri
"""
sum = 0

digitsText = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9}

def get_first_num(line):
    for character in line:
        if (character.isdigit()):
            return int(character)


    # i = 0
    # while i <= len(line):
    #     digits = list(filter(str.isdigit, line[:i]))
    #     if len(digits) > 0:
    #         return digits[0]
    #     for text, num in digitsText.items():
    #         if (line[:i].find(text) != -1):
    #             return num
    #     i += 1
        
def get_last_num(line):
    for character in line[::-1]:
        if (character.isdigit()):
            return int(character)
    # i = len(line)-1
    # while i >= 0:
    #     digits = list(filter(str.isdigit, line[i:]))
    #     if len(digits) > 0:
    #         return digits[0]
    #     for text, num in digitsText.items():
    #         if (line[i:].find(text) != -1):
    #             return num
    #     i -= 1
    

with open("day 1/input_day1_full.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    firstNum = get_first_num(line)
    lastNum = get_last_num(line)
    sum += (int(firstNum)*10 + int(lastNum))
        
print("\n" + str(sum))