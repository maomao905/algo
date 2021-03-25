from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {}
        stack = []
        for n in reversed(nums2):
            while stack and stack[-1] < n:
                stack.pop()
            
            if stack:
                greater[n] = stack[-1]
            else:
                greater[n] = -1
            
            stack.append(n)
        
        return list(greater[n] for n in nums1)

s = Solution()
print(s.nextGreaterElement([4,1,2],[1,3,4,2]))
print(s.nextGreaterElement([2,4],[1,2,3,4]))
