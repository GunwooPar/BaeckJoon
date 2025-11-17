import sys

def input():
    return sys.stdin.readline().rstrip()

max_count = 0

visited = [False] * 26 # 알파벳은 26개

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r, c, R, C, table, visited, count):

    global max_count

    if max_count < count :
        max_count = count

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < R and 0 <= nc < C and visited[ord(table[nr][nc])-65] == False :
            visited[ord(table[nr][nc])-65] = True
            dfs(nr,nc,R,C,table,visited,count+1)
            visited[ord(table[nr][nc])-65] = False



R, C = map(int,input().split())

table = []

# 테이블 제작

for _ in range(R):
    line = list(input())
    table.append(line)


visited[ord(table[0][0])-65] = True

dfs(0,0,R,C,table,visited, 1)

print(max_count)