from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N=len(nums)
        seen = set()
        res = []
        for n in nums:
            if n in seen:
                res.append(n)
            seen.add(n)
        
        for i in range(1,N+1):
            if i not in seen:
                res.append(i)
                break
        return res

"""
xor
- xor same number twice is zero
- xor all nums and 1-N leave repeated num and missing num (1missing, 3repeated num)
    - but how to get 2 number from this result
- rightmost bit to diffentiate
    - get rightmost bit x ^ -x
    - xor nums and 1-N & rightmost bit
    - it leaves one of the 2 numbers which contains the rightmost bit

space O(1)
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        def xor():
            x = 0
            for n in nums:
                x ^= n
            
            for i in range(1,N+1):
                x ^= i
            return x
        
        def xor_diff(diff):
            x = 0
            for n in nums:
                if diff & n:
                    x ^= n
            
            for i in range(1,N+1):
                if diff & i:
                    x ^= i
            return x
            
        N=len(nums)
        r = xor()
        diff = r & -r
        a = xor_diff(diff)
        
        for n in nums:
            if n == a:
                return [a, a^r]
        return [a^r, a]
        
"""
only 1-N -> use index 0 - N-1 and modify the array itself
negate the index value to mark repeated
negating twice is positive for repeated num

space O(1)
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N=len(nums)
        
        dup = 0
        for i in range(N):
            if nums[abs(nums[i])-1] < 0:
                dup = abs(nums[i])
            else:
                nums[abs(nums[i])-1] *= -1
        
        missing = 0
        for i in range(1,N+1):
            if nums[i-1] > 0:
                missing = i
        return [dup, missing]
                
s = Solution()
print(s.findErrorNums([1,2,2,4]))
print(s.findErrorNums([1,1]))
print(s.findErrorNums([2,3,2]))
        
