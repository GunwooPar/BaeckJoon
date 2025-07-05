

MAX_n = 1000000

f_table = [0] * (MAX_n+1)
   

for i in range(1,MAX_n+1):

    for j in range(i,MAX_n+1,i):

        f_table[j] += i


g_table = [0] * (MAX_n+1)

for i in range(1,MAX_n+1):
    g_table[i] = g_table[i-1] + f_table[i]


def search_y(n):
    res = 0
    
   
   

    res = g_table[n]
    

    return res

import sys

input = sys.stdin.readline


# main function

number_list = []

quantity = int(input())

for i in range(quantity):

    number = int(input())

    number_list.append(number)    



for j in number_list:
    result = search_y(j)
    print(result)


