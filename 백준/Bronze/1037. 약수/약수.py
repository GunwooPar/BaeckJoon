import sys 


input = sys.stdin.readline

def answer(divisor_list):
    min_divisor = min(divisor_list)
    max_divisor = max(divisor_list)

    return min_divisor * max_divisor





# 메인 함수 

divisor_count = int(input())

divisor_list = []



divisor_list = list(map(int, input().split()))
  


result = answer(divisor_list)

print(result)