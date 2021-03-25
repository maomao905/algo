"""
time min(3*2^(n-1), nk) space O(N)
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ('a', 'b', 'c')
        def helper(comb=[]):
            if len(comb) == n:
                nonlocal k
                k -= 1
                return ''.join(comb) if k == 0 else ''
                
            for l in letters:
                if comb and comb[-1] == l:
                    continue
                comb.append(l)
                res = helper(comb)
                if res:
                    return res
                comb.pop()
            
            return ''
        
        return helper()

"""
first character 3 ways
second to last character 2ways
-> 3 * 2^(n-1) ways in total

first  2^(n-1) -> prefix is a
second 2^(n-1) -> prefix is b
third  2^(n-1) -> prefix is c
-> we can find out the prefix given k

if we assume prefix is c,
total ways containing the prefix c is k - 2^(n-1) - 2^(n-1)
second prefix is a -> 2^(n-2) ways
second prefix is b -> 2^(n-2) ways

n = 3, k = 9
all ways ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]

2**(3-1) = 4 ways
k//4 = 2 -> c
k = k % 4ways = 1
aba, abc, aca, acb / bab, bac, bca, bcb / cab, cac, cba, cbc
                                          <-------ans------>
2**(2-1) = 2 ways
k//2 = 1//2 = 0
k = k % 2ways = 1
ab, ac / ba, bc
<-ans->

2**(1-1) = 1 ways
k // 1 = 1
b / c

time O(N) space O(1)
"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ways = 1 << n-1
        if 3*ways < k:
            return ''
        
        res = []
        cands = {'^': 'abc', 'a': 'bc', 'b': 'ac', 'c': 'ab'}
        
        res.append(cands['^'][(k-1)//ways])
        k %= ways
        k -= 1
        
        while ways > 1:
            ways >>= 1
            i, k = divmod(k, ways)
            res.append(cands[res[-1]][i])
        return ''.join(res)

s = Solution()
print(s.getHappyString(1, 3))
print(s.getHappyString(1, 4))
print(s.getHappyString(3, 9))
print(s.getHappyString(10, 100))
        
