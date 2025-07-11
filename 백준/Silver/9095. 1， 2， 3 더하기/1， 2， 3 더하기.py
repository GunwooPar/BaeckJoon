import sys

input = sys.stdin.readline

T = int(input())

test_list = []

table = [0] * (10+1)

table[1] = 1

table[2] = 2

table[3] = 4

for n in range(4,11):
    table[n] = table[n-1] + table[n-2] + table[n-3]




def dis(number):
    
    return table[number]
        


for _ in range(T):
    number = int(input())
    test_list.append((number))

for number in test_list:
    print(dis(number))
    
    