import sys

input = sys.stdin.readline

dwarf_quantity =[] 


fake_dwarf_1 = 0
fake_dwarf_2 = 0 


def find_fake_dwarf(dwarf_sum):
    for i in range(9):
        for j in range(i+1,9):
            if dwarf_sum - (dwarf_quantity[i]+ dwarf_quantity[j]) == 100:
                fake_dwarf_1 = dwarf_quantity[i]
                fake_dwarf_2 = dwarf_quantity[j]
                dwarf_quantity.remove(fake_dwarf_1)
                dwarf_quantity.remove(fake_dwarf_2)
                return dwarf_quantity


# 입력 부분 

for i in range(9):
    number = int(input().strip("\n"))
    dwarf_quantity.append(number)

# 로직 부분

dwarf_sum = sum(dwarf_quantity)


find_fake_dwarf(dwarf_sum)




    
    
dwarf_quantity.sort()


        

for i in dwarf_quantity:
    print(i)
