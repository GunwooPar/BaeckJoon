import sys

input = sys.stdin.readline

lines = []

while True:
    line = input()
    if not line:
        break
    lines.append(line)



for line in lines:

    lower_char = 0
    upper_char = 0 
    number = 0
    blink = 0

    for alphabet in line[:-1]:
        
        


        if alphabet.islower():
            lower_char += 1
        if alphabet.isupper():
            upper_char += 1
        if  alphabet.isdigit():
            number += 1
        if  alphabet.isspace():
            blink += 1

    print(f"{lower_char} {upper_char} {number} {blink}")      


