import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())

table = []

dr = [-1,1,0,0]
dc = [0,0,-1,1]


visited = [[False] * (M+1) for _ in range(N+1)]
dummy = [0] * (M+1)

table.append(dummy)

def bfs(start_r,start_c,dist):

    deq = deque([(start_r,start_c,dist)])


    while deq:

        r,c,dist = deq.popleft()

        if r == N and c == M:
            return dist

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 1 <= nr <= N and 1 <= nc <= M and visited[nr][nc] == False and table[nr][nc] == 1:
                visited[nr][nc] = True
                deq.append((nr,nc,dist+1))



for _ in range(N):
    line = list(map(int,input().strip("\n")))
    line_add = [0] + line
    table.append(line_add)


answer=bfs(1,1,1)


print(answer)