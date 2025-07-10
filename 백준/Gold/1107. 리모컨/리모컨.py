import sys

input = sys.stdin.readline

target = int(input())

M = int(input())

opt = abs(target-100)

broken = []

if M != 0:     
    broken = list(input().split())




for num in range(0,1000001):
    is_possible = True
    for N in str(num):
        if N in broken:
            is_possible = False
            break
        else:
            continue
    if is_possible == True :
        opt = min(opt,len(str(num))+abs(target-num))

print(opt)


