import sys

def input():
    return sys.stdin.readline().rstrip()


# 홀+짝 or 짝+홀 -> 짝홀 구분 그리고 
# wrong -> 짝+짝     홀+홀 
#          짝->홀    홀 ->짝 

# 시간복잡도 : N^2?



# 입력 

N = int(input())


A_list = list(map(int,input().split()))



# 순회 ?
# 1. 일단은 각각 짝 홀 구분 
# 2. i 번째와 i+1번째를 더한것을 비교 ?
#   


if N <= 1:
    print(N)

else:
    count = 1

    for i in range(0,N-1):
        if (A_list[i] % 2 ) != (A_list[i+1] % 2 ):
            count += 1

    print(count)