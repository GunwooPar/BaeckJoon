import sys
import re
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

deque_list = deque()

for _ in range(N):

    line = input()
    if "push_back" in line:

        numbers = re.findall(r'\d+', line)
        deque_list.append(int(numbers[0]))

    if "push_front" in line:

        numbers = re.findall(r'\d+', line)
        deque_list.appendleft(int(numbers[0]))

    elif line == "front":
        if len(deque_list) != 0:
            print(deque_list[0])
        else :
            print(-1)

    elif line == "back":
        if len(deque_list) != 0:
            print(deque_list[-1])
        else :
            print(-1)

    elif line == "size":
        print(len(deque_list))

    elif line == "empty":
        if len(deque_list) == 0:
            print(1)
        else:
            print(0) 

    elif line == "pop_front":
        if len(deque_list) != 0:
            pop_number = deque_list.popleft()
            print(pop_number)
        else :
            print(-1)

    elif line == "pop_back":
        if len(deque_list) != 0:
            pop_number = deque_list.pop()
            print(pop_number)
        else :
            print(-1)

