"""
grouping

min(left 0's count, 1's count) + min(1's count, right 0's count)

time O(N) space O(N)
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        nums = []
        prev = None
        cnt = 0
        for i, c in enumerate(s):
            if prev == c:
                cnt += 1
            else:
                if prev:
                    nums.append(cnt)
                cnt = 1
            prev = c
        nums.append(cnt)
        
        return sum(min(nums[i], nums[i+1]) for i in range(len(nums)-1))

s = Solution()
print(s.countBinarySubstrings('00110011'))
print(s.countBinarySubstrings('10101'))
                
        
