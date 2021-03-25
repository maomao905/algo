"""
1. except two consecutive chars so far
2. sort to get maximum
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        cnt = Counter({'a':a, 'b':b, 'c':c})
        last = ('', 0) # last character and consecutive count
        res = []
        while True:
            cur = ''
            for c, k in cnt.most_common():
                if k == 0 or (c == last[0] and last[1] == 2):
                    continue
                cnt[c] -= 1
                
                last = (c, 2 if last[0] == c else 1)
                cur = c
                break
            if not cur:
                break
            res.append(cur)
        return ''.join(res)
        
