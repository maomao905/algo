"""
(WA)
deque

1. sort requests
  [[0,1],[1,3]]
2. put (index ointo deque
  [0,1] -> deque([0,1])
  [1,3] -> popleft less than 1 and put 2, 3 into deque (greater than q[-1])
"""
from typing import List
from collections import deque, Counter
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        requests.sort()
        print(requests)
        cnt = Counter()
        q = deque()
        N=len(requests)
        for i in range(N):
            start, end = requests[i][0], requests[i][1]
            while q and q[0][0] < start:
                n, j = q.popleft()
                cnt[n] = i-j
            
            if q and q[-1][0] >= end:
                continue
            
            s = start
            if q:
                s = max(q[-1][0]+1, start)
            
            for n in range(s, end+1):
                q.append((n, i))
            
        
        while q:
            n, j = q.popleft()
            cnt[n] = N-j
        
        nums.sort()
        ans = sum(count * nums.pop() for i, count in cnt.most_common())
        return ans % (10**9+7)

"""
sweep line
O(NlogN)
"""
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N=len(nums)
        cnt = Counter()
        for s, e in requests:
            cnt[s] += 1
            cnt[e+1] -= 1
        
        res = [0] * (N+1)
        for i in range(1,N+1):
            res[i] = res[i-1] + cnt[i-1]
        
        ans = sum(c * n for c, n in zip(sorted(res, reverse=True), sorted(nums, reverse=True)))
        return ans % (10**9+7)

s = Solution()
print(s.maxSumRangeQuery([1,2,3,4,5],[[1,3],[0,1]]))
print(s.maxSumRangeQuery([1,2,3,4,5,6],[[0,1]]))
print(s.maxSumRangeQuery([1,2,3,4,5,10],[[0,2],[1,3],[1,1]]))
