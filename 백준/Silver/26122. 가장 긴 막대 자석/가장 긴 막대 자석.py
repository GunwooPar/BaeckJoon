import sys

input = sys.stdin.readline


K = int(input())

stick = []

stick = list(input().strip('\n'))

table = []

current_char = stick[0]

count = 1

for i in range(1,len(stick)):
    if stick[i] == current_char:
        count += 1

    else:
        table.append((current_char,count))

        current_char = stick[i]
        count = 1


table.append((current_char,count))

count = []

for i in range(1,len(table)) :

    count.append(2*min(table[i][1],table[i-1][1]))

if count :
    res = max(count)
else : 
    res = 0


print(res)




