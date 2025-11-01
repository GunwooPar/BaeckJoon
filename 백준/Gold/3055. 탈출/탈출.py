import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def bfs(water_q, hedgehog_q, dest_coor):
    # 물 먼저
    # 그다음 고슴도치
    dest_r, dest_c = dest_coor[0]

    time = 0


    while hedgehog_q :

        time += 1

        # 물 퍼뜨리기
        for _ in range(len(water_q)) :

            water_r , water_c = water_q.popleft()
            
            for i in range(4):
                next_water_r = water_r + dr[i]
                next_water_c = water_c + dc[i]

                if 0 <= next_water_r < R and 0 <= next_water_c < C and table[next_water_r][next_water_c] != 'X' and table[next_water_r][next_water_c] != 'D' and table[next_water_r][next_water_c] != '*':
                    table[next_water_r][next_water_c] = '*'
                    water_q.append((next_water_r,next_water_c))

        # 고슴도치 이동
        for _ in range(len(hedgehog_q)):

            r, c = hedgehog_q.popleft()

            for i in range(4):
                next_r = r + dr[i]
                next_c = c + dc[i]

                if 0 <= next_r < R and 0 <= next_c < C and table[next_r][next_c] != 'X' and table[next_r][next_c] != '*' and visited[next_r][next_c] == False :
                    visited[next_r][next_c] = True
                    if next_r == dest_r and next_c == dest_c :
                        return time
                    hedgehog_q.append((next_r,next_c))

    return "KAKTUS"
    

R, C = map(int,input().split())

visited = [[False] * C for _ in range(R)]


table = []
dest_coor = []


for _ in range(R):
    line = list(input())
    table.append(line)

water_q = deque()
hedgehog_q = deque()

for r in range(R):
    for c in range(C):
        # 고슴도치
        if table[r][c] == 'S' :
            hedgehog_q.append((r,c))
            visited[r][c] = True
        # 물 
        elif table[r][c] == '*' :
            water_q.append((r,c))

        elif table[r][c] == 'D':
            dest_coor.append((r,c))

ans = bfs(water_q,hedgehog_q, dest_coor)

print(ans)
