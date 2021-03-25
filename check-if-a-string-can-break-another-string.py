"""
beat a character by smallest character
sort and compare smallest characters

O(NlogN)
"""

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        r = None
        for c1, c2 in zip(sorted(s1), sorted(s2)):
            if c1 == c2:
                continue
            if r == None:
                r = c1 < c2
            elif (c1 < c2) != r:
                return False
        return True

s = Solution()
print(s.checkIfCanBreak('abc', 'xya'))
print(s.checkIfCanBreak('abe', 'acd'))
print(s.checkIfCanBreak('leetcodee', 'interview'))
