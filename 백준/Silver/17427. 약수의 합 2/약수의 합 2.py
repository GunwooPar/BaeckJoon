




def sum_divisor(n):
    tabul = [0] * (n+1)   

    for i in range(1,n+1):

        for j in range(i,n+1,i):

            tabul[j] += i


    return tabul


def search_y(n):
    res = 0
    
    tabul = sum_divisor(n)
    for i in range (n+1):
        res += tabul[i]
    

    return res

import sys

input = sys.stdin.readline

number = int(input())


result = search_y(number)

print(result)