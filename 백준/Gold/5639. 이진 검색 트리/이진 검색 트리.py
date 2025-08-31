import sys
sys.setrecursionlimit(10**6) # 재귀 깊이를 100만 번까지로 넉넉하게 늘려주기


def input():
    return sys.stdin.readline().rstrip()


def solve(start, end):  # (root -> left -> right) -> (left -> right -> root)
  

    # 멈춤 조건
    if start > end:
        return

    root = preorder_list[start] 
    
    # 기본적으로 오른쪽 서브 트리는 없다고 가정 
    split_point = end + 1
    for index in range(start+1, end+1):
        if preorder_list[index] > root:
            split_point = index
            
            break
            
    solve(start+1,split_point-1)


    solve(split_point,end)

    print(root)


# 이진 트리 구현(삽입) -> 메모리 초과 때문에 직접 구현 불가능 
# 후위 순회 출력

preorder_list = []


# 전위순회 입력
while True:
    try:
        
        
        preorder_list.append(int(input()))

    except :
       
        break


solve(0, len(preorder_list)-1)

