import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

dp = [-1] * (N+3)

stair = [0] 

for i in range(1,N+1):
    line = int(input())
    stair.append(line)

stair.append(0)
stair.append(0)

# 한칸 아니면 두칸 
# 세칸 연속으로 가면안됨!

# Bottom -> Up

dp[0] = stair[0]
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]

for stage in range(3, N+1) :

    
    
    # 한 계단
    temp1 = stair[stage-1] + dp[stage-3] + stair[stage]


    # 두 계단 
    temp2 = dp[stage-2] + stair[stage]

    dp[stage] = max(temp1,temp2)


res = dp[N]

print(res)