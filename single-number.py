"""
A XOR A = 0 -> duplicates will zero out
A XOR 0 = A -> single number will be left
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            
        r = 0
        for el in nums:
          # XOR
          r ^= el
        return r

s = Solution()
arr = [1, 4, 2, 1, 3, 2, 3]
print(s.singleNumber(arr))
