"""
DP
"""

from typing import List
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter()
        
        for n in nums:
            for x, y in ((n,n),(n-1,n),(n,n+1),(n-1,n-1),(n+1,n+1)):
                if cnt[x,y] > 0:
                    cnt[min(x,n), max(n,y)] = max(cnt[x,y]+1, cnt[min(x,n), max(n,y)])
            cnt[n, n] = max(cnt[n,n], 1)
        
        ans = 0
        for x, y in cnt:
            if y-x == 1:
                ans = max(cnt[x,y], ans)
        return ans

"""
simpler approach
"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        
        return max([cnt[n] + cnt[n+1] for n in cnt if cnt[n] and cnt[n+1]], default=0)

s = Solution()
print(s.findLHS([1,3,2,2,5,2,3,7]))
print(s.findLHS([1,2,3,4]))
print(s.findLHS([1,1,1,3]))
        
