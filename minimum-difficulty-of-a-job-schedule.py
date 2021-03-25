"""
memorization

time O(N^2*D)
"""

from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N=len(jobDifficulty)
        memo = {}
        def helper(i, days):
            if days == 1:
                return max(jobDifficulty[i:])
            
            if (i, days) not in memo:
                max_diff = 0
                res = float('inf')
                
                for j in range(i, N-days+1):
                    max_diff = max(jobDifficulty[j], max_diff)
                    res = min(res, helper(j+1, days-1) + max_diff)
                    
                memo[i, days] = res
                
            return memo[i, days]
        
        if N < d:
            return -1
        
        return helper(0, d)

"""
swap(dp, old)

old_best = old[i-1]
while cur_max <= jobs[i] {
    old_best = min(old_best, )
}
"""
class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        N=len(jobs)
        if N < d:
            return -1
        
        dp, old = [0] * N, [0] * N
        # fill dp for d = 1
        dp[0] = jobs[0]
        for i in range(1,N):
            dp[i] = max(dp[i-1], jobs[i])
        
        for day in range(1,d):
            dp, old = old, dp
            print(dp)
            # old best, current max, best so far
            stack = [(float('inf'),float('inf'),float('inf'))]
            for i in range(day, N):
                old_best = old[i-1]
                # stack should be decreasing
                while stack[-1][1] <= jobs[i]:
                    old_best = min(old_best, stack[-1][0])
                    stack.pop()
                stack.append([old_best, jobs[i], min(old_best + jobs[i], stack[-1][2])])
                print(stack)
                dp[i] = stack[-1][2] # best so far
                
        return dp[-1]

s = Solution()
print(s.minDifficulty([6,5,4,3,2,1], 2))
# print(s.minDifficulty([9,9,9], 4))
# print(s.minDifficulty([1,1,1], 3))
# print(s.minDifficulty([7,1,7,1,7,1], 3))
# print(s.minDifficulty([11,111,22,222,33,333,44,444], 6))
