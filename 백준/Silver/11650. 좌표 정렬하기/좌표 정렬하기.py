import sys

input = sys.stdin.readline

N = int(input())

coordinate_list = []

class Coordinate:
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)




for _ in range(N):
    x,y = list(map(int,input().split()))
    coordinate_list.append(Coordinate(x,y))



coordinate_list.sort(key= lambda coor:(coor.x,coor.y))


for coordi in coordinate_list:
    print(f"{coordi.x} {coordi.y}")
