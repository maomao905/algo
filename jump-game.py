from typing import List
"""
[2,3,1,1,4]
recursively jumping 1~x and mark 0 if it jumped to never repeat the same step again

time: O(N^2) and space: O(N)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        visited = [False] * N
        
        def jump(start, min_start):
            if start == N-1:
                return True
            elif start > N-1:
                return False
            
            end = start + nums[start]
            if end < min_start:
                return False
            
            for i in reversed(range(start+1, end+1)):
                if not visited[i] and jump(i, end+1):
                    return True
                
                visited[i] = True
            return False
        
        return jump(0, 0)

"""
DP bottom-up approach
looking from the right and check if the index is able to jump to the last index and repeat this until the left most index
 0 1 2 3 4
[2,3,1,1,4]

dp[4] -> true
dp[3] -> 3+1=4 dp[4] -> true
dp[2] -> 2+1=3 dp[3] -> true
dp[1] -> 1+3=4 dp[4] -> true
dp[0] -> 0+2=2 dp[2] -> true

 0 1 2 3 4
[3,2,1,0,4]
dp[4] -> true
dp[3] -> 0+3 = dp[3] -> false
dp[2] -> 2+1 = dp[3] -> false
dp[1] -> 2+1 = dp[3] -> false
      -> 1+1 = dp[2] -> false
dp[0] -> 3+0 = dp[3] -> false
      -> 2+0 = dp[2] -> false
      -> 1+0 = dp[1] -> false
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [False] * N
        dp[-1] = True
        
        for i in reversed(range(N-1)):
            n = nums[i]
            
            for j in range(i+1, min(i+n+1, N)):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]

"""
we only need to keep track of last good index, which can jump to the last index.
if num[i] + i can reach last good index, then we can consider the index as good index
time: O(N)
space: O(1)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        last_good_index = N-1
        
        for i in reversed(range(N-1)):
            if last_good_index <= i + nums[i]:
                last_good_index = i
        
        return last_good_index == 0

"""
keep track of furthest position it can jump

O(N)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N=len(nums)

        mx = 0
        for i in range(N):
            # never reach i
            if mx < i:
                return False

            mx = max(mx, i + nums[i])
            if mx >= N-1:
                return True

        return False

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
                
