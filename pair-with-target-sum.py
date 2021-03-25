"""
time: O(N)
space: O(1)
"""

def pair_with_targetsum(arr, target_sum):
  start, end = 0, len(arr)-1
  
  while start < end:
      if arr[start] + arr[end] == target_sum:
          return [start, end]
      
      if arr[start] + arr[end] < target_sum:
          start += 1
      else:
          end -= 1
  return [-1, -1]
 
print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
print(pair_with_targetsum([2, 6, 9, 11], 11))
