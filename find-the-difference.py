"""
tartget letter appears odd times in s and t
other letters appear even times in s and t
-> xor
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r = 0
        for _s in s:
            r ^= ord(_s)
        for _t in t:
            r ^= ord(_t)
        
        return chr(r)

s = Solution()
print(s.findTheDifference('abcddd', 'abceddd'))
