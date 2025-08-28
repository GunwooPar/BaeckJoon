import sys

def input():
    return sys.stdin.readline().rstrip()


# dfs 사용해야할듯 ?
def preorder_dfs(curr_node): 
    
    if curr_node == None:
        return 
    
    print(curr_node, end='')

    if graph[curr_node][0] :
        left_node = graph[curr_node][0]
        preorder_dfs(left_node)
    
    if graph[curr_node][1] :

        right_node = graph[curr_node][1]
        preorder_dfs(right_node)
        


def inorder_dfs(curr_node):         # 사이클이 없으므로 visited 필요없음 
    # 노드가 존재하지 않으면 종료 + leaf node 인지 판별
    if curr_node == None:
        return 
    
    # # leaf node 인지 판별 
    # if graph[curr_node] == None:
    #     # leaf node
    #     return 
    if graph[curr_node][0] :

        left_node = graph[curr_node][0]

        inorder_dfs(left_node)

    print(curr_node, end='')    # left -> root 

    if graph[curr_node][1] :

        right_node = graph[curr_node][1]

        inorder_dfs(right_node)

   

def postorder_dfs(curr_node):

    if curr_node == None:
        return

   
    if graph[curr_node][0] :

        left_node = graph[curr_node][0]
        postorder_dfs(left_node)
        

    if graph[curr_node][1] :

        right_node = graph[curr_node][1]
        postorder_dfs(right_node)
    
    print(curr_node, end='')

    

graph = {}

# input
N = int(input())


# 이진트리 노드 입력받기(부모,왼쪽자식,오른쪽자식)
for _ in range(N):
    node1 ,node2, node3 = input().split()
    


    if not node1 in graph:
  
        graph[node1] = []

    if node2 == ".":
        left_child = None
    else :
        left_child = node2

    if node3 == ".":
        right_child = None
    else:
        right_child = node3

    graph[node1] = [left_child,right_child] 


# 루트노드는 A로 고정 
preorder_dfs("A")
print()
inorder_dfs("A")
print()
postorder_dfs("A")


    

    