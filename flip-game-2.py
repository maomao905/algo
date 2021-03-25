"""
(WA)
recursion with memorization
always -- in the middle -> split and recursively -- in the middle
if sum(-- times) is odd, starting player wins, otherwise lose

++++++++++ N=10 N//2 = 5, -- at 4th,5th index
++++--++++ N=4 N//2 = 2, -- at 1th,2th index
+--+--++++ N=4 N//2 = 2, -- at 1th,2th index
+--+--+--+ no longer --

3times -> starting player won

+++++++++++ N=11 N//2 = 5, -- at 4th,5th index
++++--+++++
+--+--+++++
+--+--+--++
+--+--+----
4times -> starting player lost

"+++++++++"
"++++--+++"
"+--+--+++"
"+--+----+"

time O(logN)
"""

class Solution:
    def canWin(self, s: str) -> bool:
        def helper(n):
            if n < 2:
                return 0
            
            if n in memo:
                return memo[n]
            
            cnt = 0
            remain = (n-2)//2
            if n % 2:
                cnt = helper(remain) + helper(remain+1) + 1
            else:
                cnt = helper(remain) * 2 + 1
            
            memo[n] = cnt 
            return cnt
        
        memo = {}
        cnt = 0
        for _s in s.split('-'):
            if _s:
                cnt += helper(len(_s))
                
        return bool(cnt % 2)

"""
(WA)
"""
class Solution:
    def canWin(self, s: str) -> bool:
        def helper(n, is_first=True):
            if n < 2:
                return not is_first
            
            if (n, is_first) in memo:
                return memo[n, is_first]
            
            memo[n, is_first] = any([helper(i, not is_first) or helper(n-i-2, not is_first) for i in range(n-1)])
            return memo[n, is_first]
        
        memo = {}
        for _s in s.split('-'):
            if _s and helper(len(_s)):
                return True
                
        return False

"""
recursion with memorization
first player guarantees a win
it means there is any possiblity that first player wins, return True

without memorization N-1 * N-3 * N-5 * .. = O(N!!) double factorial
with memorization 2^(N/2)
"""        

class Solution:
    def canWin(self, s: str, memo={}) -> bool:
        n = len(s)
        if n < 2:
            return False
        
        if s not in memo:
            memo[s] = any(not self.canWin(s[:i] + '--' + s[i+2:], memo) for i in range(n-1) if s[i:i+2] == '++')
        return memo[s]
        

s = Solution()
print(s.canWin('++++'))
print(s.canWin('++'))
print(s.canWin('+++++++++++'))
print(s.canWin('+++--+-++++'))
print(s.canWin("+++++++++"))
