import sys


def is_all_ones(n):
    
    one = 1
    i = 10
    digit_count = 1
    while True:
        if one % n ==0:
            return digit_count
        one = one + i
        
        i *= 10

        digit_count += 1







input = sys.stdin.readline

bucket = [] 




if __name__ == "__main__":
    
    # 입력

    while True :
        try:
        
            line = input()

        

            number = int(line.strip())
            bucket.append(number)
        
        except:

            break

  

    for number in bucket:
         result = is_all_ones(number)
         print(result)

    
    