import heapq
import sys


class MedianFinder:
    def __init__(self):
    
        self.min_heap= []       # 중간값보다 큰값

        self.max_heap = []      # 중간값보다 작은값 

    def add_num(self, num):

        heapq.heappush(self.min_heap,num)

        # 값 역전 방지 
        if self.min_heap and self.max_heap and self.min_heap[0] < -self.max_heap[0]:

            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-value)

        # 길이 맞춤 
        if len(self.min_heap) > len(self.max_heap) +1 :
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-value)
    
        if len(self.min_heap) < len(self.max_heap) :

            value = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -value)
    
    def get_median(self):
        
        if len(self.min_heap) > len(self.max_heap) :    # 홀수일때
            
            median_num = self.min_heap[0]
        
        else:
            
            median_num = -self.max_heap[0]


        return median_num




# 메인함수 

# 입력

input = sys.stdin.readline

finder = MedianFinder()

median = []

N = int(input())

for i in range(N):

    value = int(input())

    finder.add_num(value)

    median.append(finder.get_median())


   

for i in median:

    print(i)










