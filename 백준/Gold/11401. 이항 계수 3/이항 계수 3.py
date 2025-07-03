decimal = 1000000007



fac = {0:1}

for i in range(1,4000001):
        fac[i] = (i * fac[i-1]) % decimal

def factorial(n):
    
    if n in fac :
        return fac[n]
    
   

    return fac[n]
        







def power(base,exponent):

    res = 1     # init
    while exponent>0:
        if exponent % 2 == 1:
              res = (res * base) % decimal

        base = (base * base) % decimal
        exponent //= 2

    return res

import sys




input = sys.stdin.readline


# main function

n, k = map(int,(input().split( )))

numerator = factorial(n)

# b = power(factorial(k),decimal-2) * power(factorial(n-k),decimal-2) # 이러면 너무 큰수라 터짐 

denominator = ((factorial(n-k) % decimal) * (factorial(k) % decimal)) % decimal

mod_denominator = power(denominator,decimal-2) % decimal

result = (numerator * mod_denominator) % decimal

print(f"{result}")



