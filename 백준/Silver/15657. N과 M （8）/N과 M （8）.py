import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(curr_sequence,number_list):
    if len(curr_sequence) == M:
        print(*curr_sequence)
        return 0
    
    for number in sorted(number_list):
        if not curr_sequence or number >= curr_sequence[-1]:
            curr_sequence.append(number)
            dfs(curr_sequence, number_list)
            curr_sequence.pop() 

N, M = map(int,input().split())

number_list = list(map(int,input().split()))

sequence = []

dfs(sequence,number_list)