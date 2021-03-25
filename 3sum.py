from typing import List

"""
two pointers
- sort the list
- set pivot index
- two pointers for the rest of two indices from the start and the end
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        nums.sort()
        print(nums)
        for idx in range(len(nums)):
            if nums[idx] > 0:
                break
            pivot = nums[idx]
            if idx-1 >= 0 and pivot == nums[idx-1]:
                continue
            
            l = idx+1
            h = len(nums)-1
            
            two_sum = -pivot
            while l < h:
                if nums[l] + nums[h] == two_sum:
                    result.append([pivot, nums[l], nums[h]])
                    l = self.get_next_low_position(nums, l)
                    h = self.get_next_high_position(nums, h)
                elif nums[l] + nums[h] < two_sum:
                    l += 1
                else:
                    h -= 1
        return result
    
    # skip duplicate
    def get_next_low_position(self, nums, l):
        l += 1
        while (l < len(nums)) and (nums[l] == nums[l-1]):
            l += 1
        return l
        
    # skip duplicate
    def get_next_high_position(self, nums, h):
        h -= 1
        while (h >= 0) and (nums[h] == nums[h+1]):
            h -= 1
        return h

"""
hash set
sort and skip the same number as the previous one to avoid duplicate
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hs = set(nums)
        N=len(nums)
        
        res = []
        for i in range(N):
            # because we cannot make sum of 0 with nums greater than 0
            if nums[i] > 0:
                break
            
            # skip duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # two sum
            seen = set()
            res_seen = set()
            for j in range(i+1,N):
                remain = -nums[i]-nums[j]
                # skip duplicate again
                if remain in seen and nums[j] not in res_seen:
                    res_seen.add(nums[j])
                    res.append([nums[i], nums[j], remain])
                seen.add(nums[j])
    
        return res
s = Solution()
# print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([-1,-1,-2,0,1,1,2]))
print(s.threeSum([0,0,0]))
print(s.threeSum([-5,2,3]))
# print(s.threeSum([-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]))
