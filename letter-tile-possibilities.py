class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        N=len(tiles)
        cnt = Counter(tiles)
        
        ans = 0
        def helper(i):
            if i == N:
                return 0
            
            res = 0
            for c in cnt:
                if cnt[c] > 0:
                    cnt[c] -= 1
                    res += 1
                    res += helper(i+1)
                    cnt[c] += 1
            return res
        
        memo = {}
        return helper(0)
