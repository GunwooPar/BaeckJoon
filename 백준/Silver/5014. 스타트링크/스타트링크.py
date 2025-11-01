import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def bfs(goal_floor, move, visited, deq):
    
    while deq:

        
        floor, count = deq.popleft()
        

        if floor == goal_floor :
            return count

        for i in range(2):
            next_floor = floor + move[i]

            if 1 <= next_floor <= F and visited[next_floor] == False :
                visited[next_floor] = True
                deq.append((next_floor, count+1))
                


F, S, G, U, D = map(int,input().split())

move = [U,-D]

visited = [False] * (F+1)

deq = deque()
deq.append((S,0))

count = bfs(G, move, visited,deq)



if count != None: 
    print(count)
elif count == None :
    print("use the stairs")

