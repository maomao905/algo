class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        
        N=len(s)
        l,r = 0,N-1
        while l<r:
            if s[l] != s[r]:
                return 2
            l += 1
            r -= 1
        return 1
            
