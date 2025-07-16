import sys

input = sys.stdin.readline

node_q = int(input())


edge = int(input())


graph = {}

worm_q = 0

visited = [False] * (node_q+1) 

def dfs(current_node,visited):
    global worm_q 
    visited[current_node] = True
    

    for neighbor in graph.get(current_node,[]):
        if visited[neighbor] == False:
            worm_q +=1
            dfs(neighbor,visited)
            # visited[neighbor] = False



for _ in range(edge):
    node1, node2 = map(int,input().split())

    if node1 not in graph:
        graph[node1] = []
    graph[node1].append(node2)

    if node2 not in graph:
        graph[node2] = []
    graph[node2].append(node1)
    
dfs(1,visited)

print(worm_q)