import sys

from collections import deque

input = sys.stdin.readline

dfs_ans = []

bfs_ans = []

def dfs(node1,graph,visited):
    global N
    global dfs_ans

    visited[node1] = True
    if len(dfs_ans) ==N :
        return 
    dfs_ans.append(node1)
    for neighbor in sorted(graph.get(node1,[])):

        if visited[neighbor] == False:

            dfs(neighbor,graph,visited) 
        

def bfs(start_node,graph,visited):
    deq = deque([start_node])
    global bfs_ans

    visited[start_node] = True
    bfs_ans.append(start_node)
    
    while deq :
        current_node = deq.popleft()


        for neighbor in sorted(graph.get(current_node,[])):

            if visited[neighbor] == False:

                visited[neighbor] = True
                deq.append(neighbor)
                bfs_ans.append(neighbor)
    



# main function

N, M, V = map(int,input().split())

visited = [False] * (N+1)

graph = {}

for _ in range(M):
    node1 ,node2 = map(int,input().split())
    # 양방향이므로 
    if not node1 in graph:
        graph[node1] = []
    graph[node1].append(node2)
    
    if not node2 in graph:
        graph[node2] = []
    graph[node2].append(node1)



dfs(V,graph,visited)
visited = [False] * (N+1)
bfs(V,graph,visited)

for i in dfs_ans:
    print(f"{i} ",end='')

print()


for i in bfs_ans:
    print(f"{i} ",end='')



