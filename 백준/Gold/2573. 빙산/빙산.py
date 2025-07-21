import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()

table = []

year = 0

dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs_for_counting(r,c,visited) :
    visited[r][c] = True

    deq = deque([(r,c)])

    while deq:

        r,c = deq.popleft()

        for i in range (4):
            nr = r + dr[i]
            nc = c + dc[i]

            if (0 <= nr < N) and (0 <= nc < M) and (visited[nr][nc] == False) and (table[nr][nc] > 0) :
                visited[nr][nc] = True
                deq.append((nr,nc))
            
            

# main function



N, M = map(int,input().split())



for _ in range(N):
    line = list(map(int,input().split()))
    table.append(line)


def count_iceberg(N,M,visited,table):
    count = 0
    for r in range(1,N-1):
        for c in range(1,M-1):
            if table[r][c] != 0 and visited[r][c] == False:
                bfs_for_counting(r,c,visited)
                count += 1


    return count


while True :

    visited = [[False] * M for _ in range(N)]

    num_iceburg = count_iceberg(N,M,visited,table)

    if num_iceburg >= 2 :
        print(year)
        break

    if num_iceburg == 0 :
        print(0)
        break

    melt_amount = [[0] * M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if table[r][c] > 0:
                sea_count = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < M and (table[nr][nc] == 0) :
                        sea_count += 1
                
                melt_amount[r][c] = sea_count

    
    for r in range(N):
        for c in range(M):
            table[r][c] -= melt_amount[r][c]
            if table[r][c] < 0 :
                table[r][c] = 0

    year += 1



