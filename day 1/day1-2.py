# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:43:19 2023

@author: Siri
"""

def get_first_num(line):
    for character in line:
        if (character.isdigit()):
            return int(character)
        
def get_last_num(line):
    for character in line[::-1]:
        if (character.isdigit()):
            return int(character)
    

with open("day 1/input_day1_full.txt", "r") as file:
    lines = file.readlines()
    
sum = 0
for line in lines:
    firstNum = get_first_num(line)
    lastNum = get_last_num(line)
    sum += (int(firstNum)*10 + int(lastNum))
        
print("\n" + str(sum))