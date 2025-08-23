import sys
import re
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

stack_list = deque()

for _ in range(N):

    line = input()
    if "push" in line:

        numbers = re.findall(r'\d+', line)
        stack_list.append(int(numbers[0]))

    elif line == "top" :
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[-1])
    

    elif line == "size":
        print(len(stack_list))

    elif line == "empty":
        if len(stack_list) == 0:
            print(1)
        else:
            print(0) 

    elif line == "pop":
        if len(stack_list) != 0:
            pop_number = stack_list.pop()
            print(pop_number)
        else :
            print(-1)

