import sys


def input():
    return sys.stdin.readline().rstrip()





# input 

N = int(input())

res = {}



graph = [[] for _ in range (N+1)]

# 루트부터 받지 않으면 알수없으니 리스트로 먼저 받고 그다음 부모 자식 판별 
for _ in range(N-1):
    node1, node2 = map(int,input().split())

    graph[node1].append(node2)
    graph[node2].append(node1)


# 자식, 부모
stack = [(1,0)]

while stack:
    current, parent = stack.pop()

    res[current] = parent 

    for neighbor in graph[current]:
        if neighbor != parent:
            stack.append((neighbor,current))
            


# 정답칸 (어차피 2부터 출력하면됨)
for index in range(2,N+1):
    print(res[index])



