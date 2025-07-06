import sys

input = sys.stdin.readline


N = 1000

table = [True] * (N+1)

table[0] = False
table[1] = False

for i in range(2,N+1):
    for j in range(i*2,N+1,i):
        table[j] = False


def find_prime_number(n):

    if table[n] == True:

        return 1
    return 0




# main function



quantity = int(input())

number_list = []




number_list[0:quantity] = list(map(int,input().split()))

result = 0

for i in number_list:

    result += find_prime_number(i) 


print(result)




