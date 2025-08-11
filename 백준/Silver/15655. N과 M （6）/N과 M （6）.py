import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(curr_sequence,number_list,visited):
    if len(curr_sequence) == M :
        print(*curr_sequence)
        return 0
    
    elif len(curr_sequence) == M:
        return 0
         
    
    for number in sorted(number_list):
        if number not in visited:

            if not curr_sequence or number > curr_sequence[-1]:
                visited[number] = True
                curr_sequence.append(number)
                dfs(curr_sequence, number_list, visited)
                curr_sequence.pop()
                del visited[number]



# main function

N, M = map(int,input().split())

number_list = list(map(int,input().split()))

visited = {}

sequence = []

dfs(sequence,number_list,visited)
