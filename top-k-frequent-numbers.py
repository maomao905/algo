from collections import Counter
import heapq

"""
time: O(N) + (O(logN) * 3) * N = O(NlogN)
space: O(N+K)
"""

def find_k_frequent_numbers(nums, k):
  counter = Counter(nums) # O(N)
  min_heap = []
  
  for n, cnt in counter.items():
      if len(min_heap) < k:
          heapq.heappush(min_heap, (cnt, n))
      else:
          smallest_cnt, _ = min_heap[0]
          if smallest_cnt < cnt:
              heapq.heappop(min_heap)
              heapq.heappush(min_heap, (cnt, n))
  
  return [item[1] for item in min_heap]


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
