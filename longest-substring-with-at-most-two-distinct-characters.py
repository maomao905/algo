"""
substring and two distinct chars -> sliding window

time: O(N) space: O(N)
"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        seen = defaultdict(list)
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            seen[s[i]].append(i)
            
            while len(seen) > 2:
                seen[s[start]].pop()
                if len(seen[s[start]]) == 0:
                    del seen[s[start]]
                start += 1
            max_len = max(max_len, i-start+1)
            
        return max_len

"""
time: O(N) space: O(2) = O(1)
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # store the right most index of each character
        seen = {}
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            seen[s[i]] = i
            while len(seen) > 2:
                if seen[s[start]] == start:
                    del seen[s[start]]
                start += 1
            
            max_len = max(max_len, i-start+1)
            
        return max_len

s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct('eceba'))
print(s.lengthOfLongestSubstringTwoDistinct('ccaabbb'))
print(s.lengthOfLongestSubstringTwoDistinct('abaccc'))
