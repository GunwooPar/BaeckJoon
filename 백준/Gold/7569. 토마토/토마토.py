import sys
from collections import deque

input = sys.stdin.readline

def bfs(h,r,c,day,table,deq):

    while deq :
        
        h,r,c,day = deq.popleft()


        for i in range(6):

            nr = r + dr[i]
            nc = c + dc[i]
            nh = h + dh[i]

            if 0<= nr < N and 0<= nc < M and 0<= nh < H and table[nh][nr][nc] == 0:
                table[nh][nr][nc] = 1
                deq.append((nh,nr,nc,day+1))

    for h in range(H):
        for r in range(N):
            for c in range(M):
                if table[h][r][c] == 0:

                    return -1

    return day

   

# main function

M, N, H = map(int,input().split())  # M이 가로(col) 

dr = [-1,1,0,0,0,0]
dc = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]

table = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

deq = deque()

for h in range(H):
    floor= []
    for r in range(N):
        line = list(map(int,input().split()))
        for c in range(M):
            if line[c] == 1:
                deq.append((h,r,c,0))


        floor.append(line)

    table.append(floor) 


ans = bfs(h,r,c,1,table,deq)







print(ans)