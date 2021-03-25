"""
store all elements and index pair in hashmap
check greater, smaller values as long as it can

keep track of visited element

time O(N) space O(N)
"""
from typing import List
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(list) 
        N = len(nums)
        for i in range(N):
            d[nums[i]].append(i)
        
        seen = [False] * N
        max_cnt = 0
        
        for i in range(N):
            if seen[i]:
                continue
            
            cnt = 1
            smaller = nums[i]-1
            while smaller in d:
                for j in d[smaller]:
                    seen[j] = True
                cnt += 1
                smaller -= 1
            
            larger = nums[i]+1
            while larger in d:
                for j in d[larger]:
                    seen[j] = True
                cnt += 1
                larger += 1
            
            max_cnt = max(max_cnt, cnt)
            seen[i] = True
            
        return max_cnt

"""
simpler solution
check if x-1 in the array, it does not exist, it's starting point 
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        max_cnt = 0
        for x in nums:
            if x-1 in d:
                continue
            
            cnt = 1
            y = x + 1
            while y in d:
                y += 1
                cnt += 1
            
            max_cnt = max(max_cnt, cnt)
        return max_cnt
                

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive([0,0,2]))
