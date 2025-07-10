import sys

input = sys.stdin.readline

T = int(input())

test_list = []

for i in range(T):
    M, N, x, y = map(int,input().split())
    test_list.append((M,N,x,y))




for M,N,x,y in test_list:
    if M>N:
        start_year = x
        add_year = M
    else:
        start_year = y
        add_year = N 

    limit = M*N

    found = False

    while start_year <= M*N:

        if (start_year-1) % M == x - 1 and (start_year-1) % N == y - 1:
            found = True
            break 
        
        
        start_year += add_year

    if found == True:
        print(start_year)
    else:
        print("-1")



