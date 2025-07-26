import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

string = []

string = input()

upper = {"R": 0, "O": 0, "Y": 0, "G": 0, "B": 0, "I": 0, "V":0}

lower = {"r": 0, "o": 0, "y": 0, "g": 0, "b": 0, "i": 0, "v":0}

for ch in string:
    if ch=='R' or ch=='O' or ch=='Y' or ch=='G' or ch=='B' or ch=='I' or ch=='V':
        if upper[ch] == 0:
            upper[ch] = 1


    elif ch=='r' or ch=='o' or ch=='y' or ch=='g' or ch=='b' or ch=='i' or ch=='v':
        if lower[ch] == 0:
            lower[ch] = 1



if all(value == 1 for value in upper.values()) and all(value == 1 for value in lower.values()):
    print("YeS")


elif all(value == 1 for value in upper.values()):
    print("YES")


elif all(value == 1 for value in lower.values()):
    print("yes")


else:
    print("NO!")

        



