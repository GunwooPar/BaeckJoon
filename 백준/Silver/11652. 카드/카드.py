import sys
import heapq

input = sys.stdin.readline

N = int(input())

number_list = []

dic = {}

for _ in range(N):
    number = int(input())
    number_list.append(number)


for num in number_list:

    if not num in dic:
        dic[num]= 1

    else :
        dic[num] += 1


sorted_dic=sorted(dic.items(),key= lambda dic_: (-dic_[1],dic_[0]))

print(sorted_dic[0][0])