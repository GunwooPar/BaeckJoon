import sys

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()


line = []

memo = {}

def recur(number) :

    if number == 1 :
        return 0 
    
    if number in memo :
        return memo[number]

    temp1 = number - 1

    if number % 3 == 0 :
        temp2 = min(recur(number //3),recur(temp1))

    else :
        temp2 = recur(temp1)

    if number % 2 == 0 :
        temp3 = min(recur(number//2), temp2)
    
    else :
        temp3 = temp2
    

    memo[number] = temp3 + 1


    return temp3 + 1

N = int(input())


res = recur(N)

print(res)

memo[1] = 0

while N != 1 :

    print(N, end=" ")

    
    if N % 3 == 0 and memo[N//3] == memo[N] - 1 :
        N = N // 3

    elif N % 2 == 0 and memo[N//2] == memo[N] - 1 :
        N = N // 2

    else : 
        N = N - 1

print(1)
