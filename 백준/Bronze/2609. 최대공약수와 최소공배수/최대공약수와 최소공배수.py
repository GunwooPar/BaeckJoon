import sys

input = sys.stdin.readline


def get_common_max(a,b):
    num1 = max(a,b)
    num2 = min(a,b)

    

    while num2 != 0:
        temp = num1
        num1 = num2
        num2 = temp % num2
        
        

    common_max = num1
    common_min = (a * b) // (common_max)

    return (common_max, common_min)





# main function

a, b = map(int, input().split())



common_max, common_min = get_common_max(a,b)


print(common_max)
print(common_min)