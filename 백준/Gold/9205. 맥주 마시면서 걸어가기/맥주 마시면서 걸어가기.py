import sys

sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

# 출발지에서 가장 가까운 객체? 구하기 -> if 그 거리 > 1000 : sad
                                # else : 출발지 = 그 객체 


def dfs(current_node_index,all_coors, visited):


    # 현재 노드 방문 처리 
    visited[current_node_index] = True


    current_coor = all_coors[current_node_index]

    for next_node_index in range(len(all_coors)):
        
        next_coor = all_coors[next_node_index]

        if not visited[next_node_index] and get_distance(current_coor,next_coor) <= 1000:

            dfs(next_node_index, all_coors, visited)

    

def get_distance(current_coor, next_coor):
    x = abs(current_coor[0] - next_coor[0])
    y = abs(current_coor[1] - next_coor[1])

    return x+y


flag = []

test_case = []

t = int(input())

for _ in range(t):

    # 각각 모아서 튜플로 
    store_count = int(input())

    home_coor = tuple(map(int,input().split()))

    store_coor = []
    for _ in range(store_count):
        
        store_coor_line = tuple(map(int,input().split()))
        store_coor.append(store_coor_line)

    festival_coor = tuple(map(int,input().split()))

    test_case.append((store_count,home_coor,store_coor,festival_coor))


    # 흩뿌려져있는걸 최적루트로 연결지어서 그래프 문제 방식으로 접근(거리는 가중치로 표현) 
    
    for path in test_case:
        all_coors = []      # 초기화

        all_coors.append(path[1]) # 집 좌표
    
        for coor in path[2]:
            all_coors.append(coor)

        all_coors.append(path[-1]) # 도착지 좌표 
    
        visited = [False] * (len(all_coors))

    
    dfs(0,all_coors, visited)

    if visited[-1] :
        flag.append("happy")

    else : 
        flag.append("sad")

    
for i in flag:
    print(i)


