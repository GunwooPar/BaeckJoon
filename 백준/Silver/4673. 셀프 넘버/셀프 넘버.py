import sys

def input():

    return sys.stdin.readline().rstrip()


def sum_of_digit(number:int):
    sum_num = 0
    while number != 0:
        sum_num += number % 10
        number = number // 10
    
    return sum_num

list  = []

number_set = set(list)


# set 1~10000 세팅
for i in range(1,10001):
    number_set.add(i)

# 생성자 있는 숫자 제거 

for i in range(1,10001):
    if i < 10 :
        d = i + sum_of_digit(i)
        number_set.discard(d)
    elif i < 100 :
        d = i + sum_of_digit(i)
        number_set.discard(d)
    elif i < 1000 :
        d = i + sum_of_digit(i)
        number_set.discard(d)
    elif i < 10000 :
        d = i + sum_of_digit(i)
        number_set.discard(d)
        

for number in sorted(number_set):
    print(number)

