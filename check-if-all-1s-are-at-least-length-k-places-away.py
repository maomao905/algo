from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        N=len(nums)
        last = -1
        for i in range(N):
            if nums[i] == 1:
                if last != -1 and i - last <= k:
                    return False
                last = i
        return True

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        N=len(nums)
        n = 0
        for i in range(N):
            n |= nums[i]
            if i != N-1:
                n <<= 1
        
        # remove trailing zeros
        while n:
            if n & 1 == 1:
                n >>= 1
                break
            n >>= 1
        
        cnt = 0
        while n:
            if n & 1 == 1:
                if cnt < k:
                    return False
                cnt = 0
            
            cnt += 1
            n >>= 1
        return True
            

s = Solution()
print(s.kLengthApart([1,0,0,0,1,0,0,1], 2))
print(s.kLengthApart([1,0,0,1,0,1], 2))
print(s.kLengthApart([1,1,1,1,1], 0))
print(s.kLengthApart([0,1,0,1], 1))
print(s.kLengthApart([0,0,0], 1))
