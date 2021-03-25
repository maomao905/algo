"""
brute-force O(N)
for i in range(N):
    for j in range(i,N):
        for k in range(j,N):
            pick if i<j<k

O(N^2)
arr[j] can be considered as min of i, N if arr[j] > arr[i]
for i in range(N):
    min = float(inf)
    for j in range(i,N):
        if arr[i] > arr[j]:
            continue
        if min < arr[j]:
            it's arr[k]
            return True
        else:
            min = arr[j]
"""


from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        for i in range(N):
            v_j = None
            for j in range(i+1, N):
                if nums[i] >= nums[j]:
                    continue
                
                if v_j is None:
                    v_j = nums[j]
                    continue
                
                if v_j < nums[j]:
                    # k is found
                    return True
                else:
                    # update the min as the nums[j]
                    v_j = nums[j]
        return False

""" 
if first and second are fixed third is any big number
-> focus on first and second
-> first num can be updated as long as second is true becuase third is determined by second
[1,5,-10,2]
f   s
1   5
-10 5

time: O(N)
space: O(1)
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
            
s = Solution()
# print(s.increasingTriplet([1,2,3,4,5]))
# print(s.increasingTriplet([5,3,42,1]))
# print(s.increasingTriplet([5,4,3,2,1]))
print(s.increasingTriplet([1,5,-10,2 ]))
