"""
brute-force
try all i,j,k O(N^3)

better brute-force O(N^2)
- only decide j and k and nums[i] is mininum value
    - the question is to return true/false, so as long as the 132 pattern is satisfied, we can choose any nums[i]
min-i, j, k
-1 1 3 2 0
i  j  k
-1 1  x
-1 3  2
-1 3  0
-1 2  0
"""

from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N=len(nums)
        i_val = nums[0]
        for j in range(1,N-1):
            if i_val == nums[j]:
                continue
            for k in range(j+1,N):
                if i_val < nums[k] < nums[j]:
                    return True
            i_val = min(nums[j], i_val)
        return False
        
"""
monotonic stack
store k candidates in monotonically decreasing stack (traverse in reverse order)
keep minimum values up to jth index as nums[i]

[-1,3,2,0]
nums[j]  x  3  2  
min     -1 -1 -1 -1 (nums[i])

stack = [0] # k candidates
stack values must be decreasing because if it increases, that value already becomes nums[j]
it must be nums[i] < nums[k]
if min[j] >= stack[-1], pop the elements until min[j] < stack[-1] is satisfied

time O(N) space O(N)
"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N=len(nums)
        
        # i candidates
        mins = [nums[0]]
        for n in nums:
            mins.append(min(mins[-1], n))
        
        # k candidates
        stack = [nums[-1]]
        
        # find j and k
        for j in reversed(range(1, N-1)):
            # nums[j] > nums[i]
            if nums[j] <= mins[j]:
                continue
            
            # nums[i] < nums[k]
            while stack and mins[j] >= stack[-1]:
                stack.pop()
            
            # nums[k] < nums[j]
            if stack and stack[-1] < nums[j]:
                return True
            else:
                stack.append(nums[j])
        
        return False
            
            


s = Solution()
print(s.find132pattern([1,2,3,4]))
print(s.find132pattern([3,1,4,2]))
print(s.find132pattern([-1,3,2,0]))
print(s.find132pattern([1,0,1,-4,-3]))
        
