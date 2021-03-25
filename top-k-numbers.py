import heapq

"""
heap pop O(logK)
O(NlogK)
"""

def find_k_largest_numbers(nums, k):
  heap = []
  
  for n in nums:
      if len(heap) < k:
          heapq.heappush(heap, n)
      else:
          if n > heap[0]:
              heapq.heapreplace(heap, n)
  return heap


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
