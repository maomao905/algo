import heapq
"""
time: O(NlogN)
space: O(N)
"""
def minimum_cost_to_connect_ropes(ropeLengths):
  total = 0
  heapq.heapify(ropeLengths)
  
  while len(ropeLengths) > 1:
      m1 = heapq.heappop(ropeLengths)
      m2 = heapq.heappop(ropeLengths)
      m = m1 + m2
      heapq.heappush(ropeLengths, m)
      total += m
  
  return total


def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
