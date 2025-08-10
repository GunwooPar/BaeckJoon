import sys 

def input():

    return sys.stdin.readline().rstrip()

def dfs(curr_sequence,numbers,used):

    if len(curr_sequence) == M:
        print(*curr_sequence)
        return 0
    
    for number in sorted(numbers):
        if used[number] == False:
            used[number] = True
            curr_sequence.append(number)
            dfs(curr_sequence,numbers,used)
            curr_sequence.pop()
            used[number] = False


N, M = map(int,input().split())


numbers = list(map(int,input().split()))

used = [False] * (max(numbers)+1)

sequence = []

dfs(sequence,numbers,used)

