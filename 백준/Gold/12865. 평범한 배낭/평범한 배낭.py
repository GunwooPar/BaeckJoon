import sys

class item:
    def __init__(self,weight,value):
        self.weight = weight
        self.value = value

input = sys.stdin.readline

N, W = map(int, sys.stdin.readline().split())

items = []

for _ in range(N):



    weight, value = map(int, input().split())
    items.append(item(weight,value))


quantity = N        # 물건 개수 
max_w = W           # 최대 무게 

rows = quantity + 1

cols = max_w + 1    # 무게가 0도 가능하니 

dp = [[0 for _ in range(cols)] for _ in range(rows)]    

for i in range(1,quantity+1):

    current_item = items[i-1]
    
    for w in range(max_w+1):

        

        if current_item.weight > w:
            dp[i][w] = dp[i-1][w]

        else:

            value_without_item = dp[i-1][w]    

            value_with_item = current_item.value + dp[i-1][w-current_item.weight]


            dp[i][w] = max(value_without_item, value_with_item)



print(dp[rows-1][cols-1])


