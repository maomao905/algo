"""
modify array in-place by marking visited num negative
time: O(N) space: O(1)
"""


from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            if nums[abs(n)-1] > 0:
                nums[abs(n)-1] *= -1
        
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans

s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
