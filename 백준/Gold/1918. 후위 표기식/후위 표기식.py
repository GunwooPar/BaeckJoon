import sys
import re
from collections import deque

def input():
    return sys.stdin.readline().rstrip()




infix_notation = input()

operator_list = deque()

operand_list = deque()

priority = {'*':2,'/':2,'+':1,'-':1, '(':0}

for index,char in enumerate(infix_notation):
    if char == '*' or char == '/' or char == '+' or char == '-':
        while operator_list and priority[operator_list[-1]] >= priority[char] :
                operator = operator_list.pop()
                operand_list.append(operator)

    
        operator_list.append(char)

    elif char == '(':
        operator_list.append(char)
    

    elif char == ')' :
            while operator_list and operator_list[-1] != '(' :
                operator = operator_list.pop()
                operand_list.append(operator)
            
            operator_list.pop()
            
        


    elif char.isalpha()  :
        operand_list.append(char)

while operator_list:
    operator = operator_list.pop()
    operand_list.append(operator)

# join 
result = ''.join(list(operand_list))

print(result)





