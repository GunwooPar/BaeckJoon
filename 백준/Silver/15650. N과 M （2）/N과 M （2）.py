import sys

def input():

    return sys.stdin.readline().rstrip()

def dfs(curr_sequence,j,used):

    if len(curr_sequence) == M:
        print(*curr_sequence)
        return 0

    for i in range(1,N+1):

        if used[i] == False and i>j :
            used[i] = True
            curr_sequence.append(i)
            dfs(curr_sequence,j,used)
            used[i] = False
            j = curr_sequence.pop()    
        

# main function

N, M = map(int,input().split(" "))

used = [False] * (N+1)

sequence = []



dfs(sequence,0,used)


