import sys

input = sys.stdin.readline




result = 0


N = int(input())

N_digit = len(str(N))

for i in range(1,N_digit):

    result += 9*(10**(i-1))*i


result += N_digit * (N-((10**(N_digit-1))-1))


print(result)