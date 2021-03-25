import heapq

"""
median = max of first half or min of second half
first_heap (max heap)  3
second_heap (min heap)

insert O(logN)
find O(1)
"""

class MedianOfAStream:
  def __init__(self):
      self.first_heap = [] # small numbers (max heap)
      self.second_heap = [] # large numbers (min heap)
  
  def insert_num(self, num):
      if len(self.first_heap) == 0:
          heapq.heappush(self.first_heap, -num)
          return
      
      # -3 < -1
      if self.first_heap[0] < -num:
          heapq.heappush(self.first_heap, -num)
      else:
          heapq.heappush(self.second_heap, num)
      
      if len(self.first_heap) - len(self.second_heap) > 1:
          n = heapq.heappop(self.first_heap)
          heapq.heappush(self.second_heap, -n)
      elif len(self.second_heap) - len(self.first_heap) > 1:
          n = heapq.heappop(self.second_heap)
          heapq.heappush(self.first_heap, -n)
      # print(num, self.first_heap, self.second_heap)
  
  def find_median(self):
      if len(self.first_heap) == len(self.second_heap):
          n1 = -self.first_heap[0]
          n2 = self.second_heap[0]
          return n1 + (n2-n1) / 2
      
      if len(self.first_heap) > len(self.second_heap):
          return -self.first_heap[0]
      else:
          return self.second_heap[0]


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()
