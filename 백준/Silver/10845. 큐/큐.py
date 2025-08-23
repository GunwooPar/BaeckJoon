import sys
import re
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

queue_list = deque()

for _ in range(N):

    line = input()
    if "push" in line:

        numbers = re.findall(r'\d+', line)
        queue_list.append(int(numbers[0]))

    elif line == "front":
        if len(queue_list) != 0:
            print(queue_list[0])
        else :
            print(-1)

    elif line == "back":
        if len(queue_list) != 0:
            print(queue_list[-1])
        else :
            print(-1)

    elif line == "size":
        print(len(queue_list))

    elif line == "empty":
        if len(queue_list) == 0:
            print(1)
        else:
            print(0) 

    elif line == "pop":
        if len(queue_list) != 0:
            pop_number = queue_list.popleft()
            print(pop_number)
        else :
            print(-1)

