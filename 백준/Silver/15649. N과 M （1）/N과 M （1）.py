import sys 

def input():

    return sys.stdin.readline().rstrip()

def dfs(curr_sequence,used):
    
    if len(curr_sequence) == M:
        print(*curr_sequence)
        return 0

    for i in range(1,N+1):

        if used[i] == False:
            used[i] = True
            curr_sequence.append(i)
            dfs(curr_sequence,used)
            curr_sequence.pop()
            used[i] = False
            
        

# main function

N, M = map(int,input().split(" "))

used = [False] * (N+1)

sequence = []

dfs(sequence,used)

