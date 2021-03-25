class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N=len(nums)
        l = 0
        for r in range(1,N):
            if nums[l] < nums[r]:
                l += 1
                nums[l] = nums[r]
                
        return l+1
