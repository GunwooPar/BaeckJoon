import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()


"""
4칸 탐색시도 -> 후진시도 -> 
"""


def dfs(curr_coor, direction, visited):
    # dfs드갈때 마다 +1
    r, c = curr_coor

    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    # 경계점인지 아닌지, 벽 유무, 방문여부 
        # 청소와 방문처리
    visited.add(curr_coor)


    # 2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    # direction 보존 해야하기 때문에 임시 변수 선언 
    temp_direction = direction
    for _ in range(4):
        
        # 1. 반시계 방향으로 90도 회전한다.(나머지연산(모듈러연산) 이용해 반시계 90도 회전 구현)
        # 회전이라 원래 방향 변경 
        temp_direction = (temp_direction+3) % 4
        next_r = r + dr[temp_direction]
        next_c = c + dc[temp_direction]

        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우("청소되지않은"이라는 조건이 있으므로 visited 여부 확인)
        if 0 <= next_r < N and 0 <= next_c < M and board[next_r][next_c] != 1 and (next_r,next_c) not in visited:
        
            dfs((next_r, next_c), temp_direction, visited)

            # 후진 로직 실행하지 않도록 즉시 return
            # 할일 마친거      
            return 
        
    # 후진 로직 
    # 원래 방향(direction)을 기준으로 뒤쪽 계산
    back_r = r - dr[direction]
    back_c = c - dc[direction]

    # 청소기는 이미 청소한 칸에 후진가능  
    if 0 <= back_r < N and 0 <= back_c < M and board[back_r][back_c] != 1:
        # 후진시에는 원래 방향 유지!        
        dfs((back_r, back_c), direction, visited)
    # 다해봤는데 안된다는거 
    return 

    


board = []

dr = [-1,0,1,0]
dc = [0,1,0,-1]

visited = set()

N, M = map(int,input().split())

init_r, init_c, direction = map(int,input().split())

init_coor = (init_r, init_c)


for _ in range(N):

    line = list(map(int,input().split()))
    board.append(line)

dfs(init_coor, direction, visited)

print(len(visited))





