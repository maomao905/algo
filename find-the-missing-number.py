# def find_missing_number(nums):
#     arr = [0] * (len(nums) + 1)
#     for n in nums:
#         arr[n] = 1
# 
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             return i
#     return -1
"""
use cyclic sort
time: O(n)
space: O(1)
"""
def find_missing_number(nums):
    i = 0
    while i < len(nums):
        val = nums[i]
        if val < len(nums) and nums[i] != nums[val]:
            nums[i], nums[val] = nums[val], nums[i]
        else:
            i += 1
    print(nums)
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return -1

print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
