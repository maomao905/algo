"""
{xxx}

copy current list and append the character inside brackets

time: O(N^N)
space: O(N^N)
        
"""

from typing import List
class Solution:
    def expand(self, s: str) -> List[str]:
        cur = [['']]
        i = 0
        while i < len(s):
            if s[i] == '{':
                chars = []
                i+=1
                # extract characters inside the brackets
                while True:
                    if s[i] == ',':
                        i += 1
                        continue
                    elif s[i] == '}':
                        break
                    else:
                        chars.append(s[i])
                    i += 1
                
                new_cur = []
                for _cur in cur:
                    for c in sorted(chars):
                        cur_cp = list(_cur)
                        cur_cp.append(c)
                        new_cur.append(cur_cp)
                cur = new_cur
            else:
                for c in cur:
                    c.append(s[i])
            
            i += 1
        
        res = [''] * len(cur)
        for i in range(len(cur)):
            res[i] = ''.join(cur[i])
        return res

class Solution:
    def expand(self, s: str) -> List[str]:
        def get_cands(i):
            cands = []
            last = 0
            for j in range(i+1,N):
                if s[j] == ',':
                    continue
                if s[j] == '}':
                    last = j
                    break
                cands.append(s[j])
            return cands, last
        
        def helper(i, comb):
            # print(i,comb)
            if i == N:
                return [''.join(comb)]
            
            res = []
            if s[i] == '{':
                cands, i = get_cands(i)
                for c in sorted(cands):
                    comb.append(c)
                    res.extend(helper(i+1, comb))
                    comb.pop()
                return res
            else:
                comb.append(s[i])
                res.extend(helper(i+1, comb))
                comb.pop()
            return res
        
        N=len(s)
        return helper(0, [])

"""
recursion
it doesn't need backtrack because string is immutable
worst case is repeat {a,b} -> 2^N * N (string copy)
"""

class Solution:
    def expand(self, S: str) -> List[str]:
        
        def helper(s, word):
            if not s:
                res.append(word)
                return
            if s[0] == '{':
                j = s.find('}')
                for char in sorted(s[1:j].split(',')):
                    # O(N) for slice and concatnation
                    helper(s[j+1:], word + char)
            else:
                helper(s[1:], word + s[0])
        res = []
        helper(S, '')
        return res
        
s = Solution()
print(s.expand("{a,b}{a,b}{a,b}{a,b}"))
# print(s.expand("abcd"))
