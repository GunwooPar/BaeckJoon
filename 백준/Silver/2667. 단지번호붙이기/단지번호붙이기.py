import sys

input = sys.stdin.readline



table = []





dr = [-1,1,0,0]
dc = [0,0,-1,1]


def dfs(r,c,visited,total_apart,i):
    visited[r][c] = True

    for index in range(4):
        nr = r + dr[index]
        nc = c + dc[index]

        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False and table[nr][nc] == 1 :
            total_apart[i] += 1
            dfs(nr,nc,visited,total_apart,i)


    





# main function

N = int(input())

visited = [[False] *(N) for _ in range(N)]

total_apart = [0] * ((N*N)+1)

for _ in range (N):
    line = list(map(int,input().strip("\n")))
    table.append(line)

for r in range(N):
    for c in range(N):
        if visited[r][c] != True and table[r][c]==1:
            for i in range(1,N*N):
                if total_apart[i] == 0:
                    total_apart[i] = 1
                    dfs(r,c,visited,total_apart,i) 
                    break

           

first_line = 0

for i,value in enumerate(total_apart):
    if value == 0 and i !=0:
        first_line = i-1
        print(first_line)

        break

results = []
for count in total_apart:
    if count>0:
        results.append(count)

results.sort()

for res in results:
    print(res)