"""
requirements:
start with two letters
max len 6, min len 2
numbers not in middle, only at end, first number used not 0
no periods, spaces or punc marks allowed
"""
import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
        #s=CS50
        if len(s) < 2 or len(s) > 6: #s bigger 4 and smaller then 6 -> skip
            return False
        if s[0].isdigit() or s[1].isdigit(): # s[0]=C, s[1]=S => is digit : False -> skip
            return False
        if not s.isalnum(): #not is alnum (alpha, num (special char)) -> CS50 -> no Special Char -> skip
            return False
        #check if after index 1 and before index -1(from reverse) is any char (with for loop through the string)
        #any function return value -> bool
        if lookZero(s) == True:
            return False
        return True

def lookZero(s):
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

main()