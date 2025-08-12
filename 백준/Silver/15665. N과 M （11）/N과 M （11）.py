import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(curr_sequence):
    if len(curr_sequence) == M :
        print(*curr_sequence)
        return 0
    
    for number in number_list:
        curr_sequence.append(number)
        dfs(curr_sequence)
        curr_sequence.pop()

N, M = map(int,input().split())

number_list = sorted(set(map(int,input().split())))

sequence = []


dfs(sequence)