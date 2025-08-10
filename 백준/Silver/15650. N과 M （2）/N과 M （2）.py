import sys

def input():

    return sys.stdin.readline().rstrip()

def dfs(curr_sequence,k,used):

    if len(curr_sequence) == M:
        print(*curr_sequence)
        return 0

    for i in range(k+1,N+1):
            
            if i not in curr_sequence:
                curr_sequence.append(i)
                dfs(curr_sequence,k,used)
                k = curr_sequence.pop()    
        

# main function

N, M = map(int,input().split(" "))

used = [False] * (N+1)

sequence = []



dfs(sequence,0,used)


