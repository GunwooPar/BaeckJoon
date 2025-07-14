import sys

input = sys.stdin.readline

dr = [-1,1,0,0]

dc = [0,0,-1,1]

N, M = map(int,input().split())

visited = [[False]*M for _ in range(N)]

answer = 0

def dfs(r,c,depth,current_sum):
    global answer

    if depth==4:
        answer = max(answer,current_sum)
        return  
    
    for i in range(4):
        nr = r  + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc]==False:
            visited[nr][nc] = True
            dfs(nr,nc,depth+1,current_sum+table[nr][nc])
            visited[nr][nc] = False
          
def check_t_shape(r,c):

    global answer
    center_value = table[r][c]
    valid_neighbors = []

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if  0 <= nr < N and 0 <= nc < M:
            
            valid_neighbors.append(table[nr][nc])



    if len(valid_neighbors) == 3:
        current_sum = center_value + sum(valid_neighbors)
        answer = max(current_sum, answer)

    elif len(valid_neighbors) == 4:
        
        for i in range(4):
            current_sum = center_value + sum(valid_neighbors) - valid_neighbors[i]
            answer = max(answer, current_sum)
        


# main function


table = []

for _ in range(N):
    line_list = list(map(int,input().split()))
    table.append(line_list)

for r in range(N):
    for c in range(M):

        visited[r][c] = True
        dfs(r,c,1,table[r][c])
        visited[r][c] = False
        check_t_shape(r,c)


print(answer)



