import heapq
import math

"""
closest points -> smallest distance -> max-heap
time: O(NlogK)
space: O(K)
"""

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def dist_from_origin(self):
    return math.sqrt(self.x**2 + self.y**2)

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

def find_closest_points(points, k):
  heap = []
  
  for p in points:
      dist = p.dist_from_origin()
      if len(heap) < k:
          heapq.heappush(heap, (-dist, p))
      elif -dist > heap[0][0]:
          heapq.heappop(heap)
          heapq.heappush(heap, (-dist, p))
          
  return [h[1] for h in heap]
  

def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()
