from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N=len(nums)
        L=[nums[0]]*N
        for i in range(1,N):
            L[i] = L[i-1]*nums[i]
        
        R=[nums[-1]]*N
        for i in reversed(range(N-1)):
            R[i] = R[i+1]*nums[i]
        
        res = [0] * N
        for i in range(N):
            l = L[i-1] if i >= 1 else 1
            r = R[i+1] if i+1 < N else 1
            res[i] = l*r
        return res

s = Solution()
print(s.productExceptSelf([1,2,3,4]))
        
        
        
