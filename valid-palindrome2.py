"""
brute-force O(N^2) -> TLE
delete character one by one and check if it's palindrome
    - loop N times
        - string concatnation O(N)
        - palindrome check O(N)
"""

class Solution:
    def is_palindrome(self, s):
        center = 0
        if len(s) % 2 == 1:
            center = len(s) // 2
        else:
            center = len(s) // 2
            if s[center] != s[center-1]:
                return False
        
        for i in range(center):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
    
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            if self.is_palindrome(s[:i] + s[i+1:]):
                return True
        return False

"""
delete character when necessary
O(N)
traverse from beginning and end, and check if both characters are the same,
and if it's not the same, we can remove one character from left side or right side
we try both cases, if neither is palindrome, it's false
"""
class Solution:
    def is_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        for i in range(N//2):
            j = N-i-1
            if s[i] != s[j]:
                return any([self.is_palindrome(s, i+1, j), self.is_palindrome(s, i, j-1)])
        return True
                

s = Solution()
print(s.validPalindrome('aba'))
print(s.validPalindrome('abca'))
            
