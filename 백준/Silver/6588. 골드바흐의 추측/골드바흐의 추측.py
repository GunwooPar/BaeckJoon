import sys 

import math

input = sys.stdin.readline

table = []

max_n = 1000000


prime_list= [True] * (max_n+1)

prime_list[0] = False
prime_list[1] = False


for i in range(2,int(math.sqrt(max_n))+1):
    if prime_list[i] == True:
        for j in range(2*i,max_n+1,i):
            prime_list[j] = False 

prime_list[2] = False # 짝수면서 소수니까 X


# main function

while True:
    
    number = int(input())
    if number == 0 :
        break
    table.append(number)
   




for n in table:             # 8 20 42
    for i in range(3,n):
        if prime_list[i] and prime_list[n-i]:
            print(f"{n} = {i} + {n-i}")
            break


