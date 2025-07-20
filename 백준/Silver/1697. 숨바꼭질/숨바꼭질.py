import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

max_num = 100000

visited = [False] * (max_num+1)


def bfs(start_num,count,target,visited):

   


    visited[start_num] = True

    deq = deque([(start_num,count)])

    
    
    while deq:
        current_num,count = deq.popleft()

        if (current_num == target):


            return count


        for i in range(3):
            dn = [1,-1,current_num]
            next_num = current_num + dn[i]

            if  0 <= next_num <= max_num  and visited[next_num] == False:
                visited[next_num] = True
                deq.append((next_num,count+1))
                


# main function

N, K = map(int,input().split())

    
ans = bfs(N,0,K,visited)


print(ans)