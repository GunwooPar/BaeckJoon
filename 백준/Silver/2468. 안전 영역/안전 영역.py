import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

"""
dfs 이용
끝까지 도달후 갯수 세기

덩어리 갯수 세기 

최적화 생각해서 visited 비슷한거 넣으면 굳이 다 방문 안해도될거 같지만 
잘하면 그게 더 오래 걸릴 여지도 있음 
"""
# 북동남서
dr = [-1,0,1,0]
dc = [0,1,0,-1]




def dfs_for_counting(coor, visited, rain_fall):

    r ,c = coor 
    
    
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and (nr,nc) not in visited and table[nr][nc] > rain_fall :
            visited.add((nr,nc))
            dfs_for_counting((nr,nc),visited, rain_fall)

    return 1


visited = set()

table = []

N = int(input())

for _ in range(N):
    line = list(map(int,input().split()))
    table.append(line)


# 최댓높이구하는 로직?

max_height = max(map(max, table))

max_sum = 0

for rain_fall in range(max_height):
    sum = 0
    for r in range(N):
        for c in range(N):
            if (r,c) not in visited and table[r][c] > rain_fall:
                sum += dfs_for_counting((r,c), visited,rain_fall)
            
    visited = set()

    if sum > max_sum :
        max_sum = sum


print(max_sum)