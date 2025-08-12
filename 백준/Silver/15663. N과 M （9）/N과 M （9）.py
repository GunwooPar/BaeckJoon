import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(curr_sequence,number_list,visited):
    if len(curr_sequence) == M:
        print(*curr_sequence)
        return 0
    
    last_num = -1
    for index in range(N):
        
        if not visited[index]  and last_num != number_list[index]:  
            curr_sequence.append(number_list[index])
            visited[index] = True
            last_num = number_list[index]
            dfs(curr_sequence, number_list,visited)
            curr_sequence.pop()
            visited[index] = False




# main function

N, M = map(int,input().split())

number_list = sorted(list(map(int,input().split())))

sequence = []

visited = [False] * (N)

dfs(sequence,number_list,visited)