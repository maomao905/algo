"""
power set
dynamic programming
prevの答えを使ってnextを求める
"""
from typing import List
# from collections import deque
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         ans = []
#         level1 = [(i, [nums[i]]) for i in range(len(nums))]
#         q = deque(level1)
# 
#         while len(q) > 0:
#             i, val  = q.popleft()
#             ans.append(val)
# 
#             if i >= len(nums) - 1:
#                 continue
# 
#             for j in range(i+1, len(nums)):
#                 q.append((j, val + [nums[j]]))
# 
#         ans.append([])
#         return ans
"""
choose each element or not (binary choice)
time: O(2^N) choices * O(N) list deep copies = O(N*2^N)
space: O(2^N*N) choices * N elements each time
"""
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         output = [[]]
# 
#         for num in nums:
#             print(output)
#             output += [curr + [num] for curr in output]
# 
#         return output

"""
backtrack
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        N=len(nums)
        def recursive(i, comb=[]):
            res.append(list(comb))
            
            for j in range(i, N):
                comb.append(nums[j])
                recursive(j+1, comb)
                comb.pop()
        
        recursive(0)
        return res

"""
bitmask
2**n通りの0,1を生成
zero left paddingを行うことで1ではなく001にする(nth_bit)
time: (N * 2^N)
space: O(N * 2^N)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nth_bit = 1 << N
        
        ans = []
        for i in range(2**N):
            bitmask = bin(i|nth_bit)[3:]
            ans.append([nums[j] for j in range(N) if bitmask[j] == '1'])
        
        return ans



s = Solution()
print(s.subsets([1,2,3]))
        
        
