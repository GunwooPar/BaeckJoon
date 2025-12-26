import sys

sys.setrecursionlimit(10**6)

def input():

    return sys.stdin.readline().rstrip()

infinity = float('inf')

memo = {}

# dp ㄱㄱ 
# 메모이제이션 감안 
def recur(target, sum, sorted_coin_list):

    global infinity

    global memo


    current_min = infinity
    
    for coin in sorted_coin_list :

        if sum == target :
            return 0
        
        if sum in memo :
            return memo[sum]

        

        if (target - sum) >= coin :
            current_min = min(recur(target, sum+coin, sorted_coin_list), current_min)
            
    memo[sum] = current_min + 1

    return current_min + 1



        

            
            


n, k = map(int,input().split())

memo[k] = 0

coin_list = []

for _ in range (n) :
    line = int(input())
    coin_list.append(line)

sorted_coin_list = sorted(coin_list) # 오름차순 정렬 


res = recur(k, 0, sorted_coin_list)

if res != infinity :
    print(res)

else :
    print(-1)