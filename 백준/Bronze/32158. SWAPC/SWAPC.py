import sys

def input():

    return sys.stdin.readline().rstrip()





length = int(input())


string = input()


table = [[],[]]                      # 2행 100열 

for index,c in enumerate(string):
    if c == 'P':
        table[0].append(index)    
    if c == 'C':
        table[1].append(index)

# 문자열 리스트화

s_list = list(string)


# get min_count

p_count = 0

c_count = 0

for c in table[0]:
    if c == None:
        break
    p_count += 1

for c in table[1]:
    if c == None:
        break
    c_count += 1


min_count = min(p_count,c_count)


# swap

for i in range(min_count):
    p_index = table[0][i]
    c_index = table[1][i]


    s_list[p_index], s_list[c_index] = s_list[c_index], s_list[p_index]

result = "".join(s_list)

print(result)
