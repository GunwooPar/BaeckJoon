import sys

input = sys.stdin.readline


N = int(input().strip())

table = []

sum = 0




def find_longest(line):    # row, col: 아래나 오른쪽 적용된애들 
   
    current_count = 1
    max_count = 1
    for i in range(0,len(line)-1):
        if line[i] == line[i+1]:
            current_count += 1
        else:       # 끊겼을때
            max_count = max(current_count, max_count)
            current_count = 1
    max_count = max(current_count, max_count)        
        
    return max_count






def traversal():
    max_count_down = 0
    max_count_right = 0
    result = 0

    # 초기 상태 검사
    for row in table:
        max_count = find_longest(row)
        result = max(result,max_count)

   
    for i in range (N):
        for j in range(N):
            
            # 중복되는거 고려해서 아래와 오른쪽만 고려

                # 아래
            if i+1 < N and table[i][j] != table[i+1][j]:
                table[i][j], table[i+1][j] = table[i+1][j], table[i][j]
                row1 = table[i]
                row2 = table[i+1]
                col1 = [table[r][j] for r in range(N)]
                max_count_down = max(find_longest(row1),find_longest(row2),find_longest(col1))
                if max_count_down == N:
                    result = max_count_down
                    return result
                if result < max_count_down:
                    result = max_count_down
                table[i][j], table[i+1][j] = table[i+1][j], table[i][j]    # 되돌림 
            
                
                



                # 오른쪽 
            if j+1 < N and table[i][j] != table[i][j+1]:
                table[i][j], table[i][j+1] = table[i][j+1], table[i][j]
                row1 = table[i]
                col1 = [table[r][j] for r in range(N)]
                col2 = [table[r][j+1] for r in range(N)]
                max_count_right = max(find_longest(row1),find_longest(col1),find_longest(col2))
                if max_count_right == N:
                    result = max_count_right
                    return result

                if result < max_count_right:
                    result = max_count_right
                table[i][j], table[i][j+1] = table[i][j+1], table[i][j]    # 되돌림  
                
            
            
            
            max_count = max(max_count_down,max_count_right)


    return result
                               
          
   
         
# main function
   
# 입력 부분 
for _ in range(N):
        row = list(input().strip("\n"))
        table.append(row)

result = traversal()


                   
print(result)




