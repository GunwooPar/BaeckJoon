import sys
# 재귀 깊이 제한 늘려주기 
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()


# 임의의점에서 최대거리 ~ 지름 양끝 중 일부 노드 -> 지름 양끝 중 일부노드에서 최대거리 -> 지름   
# 최대거리와 최대거리인 노드 


def dfs(graph, node, V, visited, current_sum):

    farthest_info = (current_sum, node)

    for neighbor, weight in graph[node]:
        if neighbor not in visited:
            
            visited.add(neighbor)
            result_from_child = dfs(graph, neighbor, V, visited, current_sum + weight)
            
            if result_from_child[0] > farthest_info[0] :
                farthest_info = result_from_child

            # 백트레킹 로직
            visited.remove(neighbor)
    
    return farthest_info
    

# 입력 

V = int(input())


graph = {}

visited = set()

max_path_weight = 0

for i in range(1,V+1):
    graph[i] = []

# 그래프 형성 

for _ in range(V):
    

    stream_list = list(map(int,input().split()))
    startNode = stream_list[0]

    i = 1
    while stream_list[i] != -1:
        neighborNode, weight = stream_list[i], stream_list[i+1]
        
        # 튜플형태로 묶기
        graph[startNode].append((neighborNode,weight))
        i += 2

# 임의의 노드 하나 넣기 (1)
visited = {1}
_, farthest_node_A = dfs(graph,1, V, visited, 0)


# init 
visited = {farthest_node_A}

diameter, _ = dfs(graph,farthest_node_A, V, visited, 0)


print(diameter)




