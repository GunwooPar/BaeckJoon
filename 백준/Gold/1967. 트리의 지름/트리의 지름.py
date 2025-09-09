import sys

from collections import defaultdict

sys.setrecursionlimit(10**6)

def input() :
    return sys.stdin.readline().rstrip()

def dfs(graph, start_node,visited, current_sum):
    farthest_info = (start_node, current_sum)
    
    # 탐색로직
    for neighbor, weight in graph[start_node]:
        if neighbor not in visited:
            visited.add(neighbor)
            result_from_child = dfs(graph, neighbor,visited,current_sum+weight)
            
            if result_from_child[1] > farthest_info[1] :
                farthest_info = result_from_child


            # 백트래킹 로직 
            visited.remove(neighbor)            

    return farthest_info
            

graph = defaultdict(list)

visited = set()

# input
N = int(input())

for _ in range(N-1):
    line = list(map(int,input().split()))
    parent_node = line[0]

    graph[parent_node].append((line[1],line[2]))
    graph[line[1]].append((parent_node,line[2]))

visited = {1}
A_node, _ = dfs(graph, 1, visited, 0)
visited = {A_node}
_, diameter = dfs(graph, A_node, visited, 0)

print(diameter)
