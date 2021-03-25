"""
sort nums in-place in O(n)
swap: index=2のvalueをindex0に
      index0=3 -> index 3-1=2
"""

def cyclic_sort(nums):
  for i in range(len(nums)):
      val = nums[i]
      nums[i], nums[val-1] = nums[val-1], nums[i]
  return nums
 
print(cyclic_sort([3, 1, 5, 4, 2]))
