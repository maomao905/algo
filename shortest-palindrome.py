"""
move pivot to left every 0.5 step
when <n left string> == <n right string>, it becomes palindrome
rolling hash to get hash in O(1) in every step

O(N)
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N=len(s)
        need = []
        """
        x x x x
        x x x x x
        """
        is_odd = N%2
        pivot = N//2 if is_odd else N//2 - 1
        
        left_start = pivot-1 if is_odd else pivot
        right_start = pivot+1 if is_odd else pivot+1
        
        W = 26
        MOD = 2**32
        l_h = 0
        for i in reversed(range(left_start+1)):
            l_h += (l_h * W + ord(s[i]))%MOD
        
        r_h = 0
        for i in range(right_start, N):
            r_h += (r_h * W + ord(s[i]))%MOD
        
        print(l_h, r_h, pivot)
        r = N-1
        while 0 < pivot and l_h != r_h:
            is_odd = not is_odd
            
            if is_odd:
                l_h = (l_h - (pivot ** W) * ord(s[pivot]))%MOD
                r_h -= ord(s[r])
            else:
                pivot -= 1
                r_h = (r_h - ord(s[r]) + (pivot ** W) * ord(s[pivot+1]))%MOD
            
            r -= 1
        if is_odd:
            r = s[pivot+1:]
            return r[::-1] + s[pivot] + r
        else:
            r = s[pivot:]
            return r[::-1] + r

s = Solution()
# print(s.shortestPalindrome('aacecaa'))
print(s.shortestPalindrome('aacecaaa'))
                
        
        
        
