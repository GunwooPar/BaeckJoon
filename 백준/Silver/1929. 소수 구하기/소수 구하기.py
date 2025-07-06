import sys

input = sys.stdin.readline

Max_n = 1000000

table = [True] * (Max_n+1)

table[0] = False
table[1] = False

for i in range(2,Max_n+1):
    if table[i] == True:
        for j in range(i*2,Max_n+1,i):
            table[j] = False



def find_prime_number(M,N):
    prime_table = []

    for i in range(M,N+1):

        if table[i]  == True:
            prime_table.append(i)
           


    return prime_table






M, N = map(int,input().split())

result_table = []


result_table = find_prime_number(M,N)

for i in result_table:
    print(i)