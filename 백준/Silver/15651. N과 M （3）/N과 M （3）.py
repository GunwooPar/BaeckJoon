import sys

def input():

    return sys.stdin.readline().rstrip()

def dfs(curr_sequence):

    if len(curr_sequence) == M:
        print(*curr_sequence)
        return 0

    for i in range(1,N+1):
        curr_sequence.append(i)
        dfs(curr_sequence)
        curr_sequence.pop()

N, M = map(int,input().split())

sequence = []

dfs(sequence)