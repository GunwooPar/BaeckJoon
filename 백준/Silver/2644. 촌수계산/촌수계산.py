import sys

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip() 


def dfs(start_node, target_node, visited,current_sum):
    # 종료 조건 (target노드 만났을때)
    if start_node == target_node :
        return current_sum
    
    # 방문처리
    visited.add(start_node)

    

    # 탐색 로직     
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            visited.add(neighbor)
            # 다시 호출한 쪽으로 반환 !!
            result_from_path = dfs(neighbor, target_node, visited, current_sum+1)
            
            if result_from_path != -1:
                return result_from_path

    # 결과 로직
    return -1



visited = set()

graph = {}

n = int(input())

start_node, target_node = map(int,input().split())

m = int(input())

for _ in range(m):

    x, y = map(int,input().split())

    if x not in graph:
        graph[x] = []

    graph[x].append(y)

    if y not in graph:
        graph[y] = []

    graph[y].append(x)



res = dfs(start_node, target_node,visited, 0)

print(res)