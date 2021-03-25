"""
s[i:j]s[i:j]s[i:j] in s[i+1:j]s[i:j]s[i:j]s[i:j]s[i:j]s[i:j-1]
s[i:j]s[i:j]s[i:k] in s[i+1:j]s[i:j]s[i:k]s[i:j]s[i:j]s[i:k-1]
abcabcabcabc in bcabcabcabcabcabcabcab

O(N) in average, O(N^2) in worst
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]

s = Solution()
print(s.repeatedSubstringPattern('abab'))
print(s.repeatedSubstringPattern('aba'))
print(s.repeatedSubstringPattern('abcabcabc'))
print(s.repeatedSubstringPattern('bbbc'))
