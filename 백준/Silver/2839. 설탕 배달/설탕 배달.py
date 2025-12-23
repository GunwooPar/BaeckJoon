import sys 

def input():
    return sys.stdin.readline().rstrip()

infinity = float('inf')


def recur(number,dp):

    global infinity 
    # 종료조건 
    if number == 0 :
        
        return 0
    
    if number < 0 :
        return  infinity

    if dp[number] != -1 :
        return dp[number]

    curr_count = min(recur(number-5,dp) , recur(number-3,dp)) + 1
    dp[number] = curr_count

    return curr_count



# 5, 3 

N = int(input())

dp = [-1] * (N+1)

res = recur(N,dp)

if res == infinity :
    print(-1)
    
else :
    print(res)

