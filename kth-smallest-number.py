import heapq

def find_Kth_smallest_number(nums, k):
  heap = []
  
  for n in nums:
      if len(heap) < k:
          heapq.heappush(heap, -n)
      if -n > heap[0]:
          heapq.heappop(heap)
          heapq.heappush(heap, -n)
  # TODO: Write your code here
  if len(heap) < k:
      return -1
  
  return -heap[0]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
