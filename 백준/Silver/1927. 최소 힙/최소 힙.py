import sys
from heapq import heappush, heappop

def input():
    return sys.stdin.readline().rstrip()


N = int(input())


heap = []

res = []

for _ in range(N):
    x = int(input())
    
    if x == 0:
        if len(heap) == 0:
            res.append(0)
            continue
        min = heappop(heap)
        res.append(min)

    else :
        heappush(heap,x)


for number in res:
    print(number)