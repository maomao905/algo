"""
225
2/2/5, 2/25, 22/5, 225
100
1/00, 10/0, 100

12345
123/ -> impossible
less than two chars and less than 26, greater than 0でrecursive
=> TLE
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(start):
            nonlocal cnt
            # goal
            if start >= N:
                cnt += 1
                return
            
            for end in range(start, N):
                # constraint
                n = int(s[start:end+1])
                if 0 < n <= 26:
                    dfs(end+1)
                else:
                    break
            return
        
        cnt = 0
        N = len(s)
        dfs(0)
        return cnt

"""
recursion + memorization
time: O(N) since we never go through no more than 2 chars and use memo
space: O(N) for memo
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(start):
            if start >= N:
                return 1
            
            if start in memo:
                return memo[start]

            cnt = 0
            for end in range(start, N):
                n = int(s[start:end+1])
                if 0 < n <= 26:
                    cnt += dfs(end+1)
                else:
                    break

            memo[start] = cnt
            return cnt

        memo = {}
        N = len(s)
        return dfs(0)

s = Solution()
print(s.numDecodings('12'))
print(s.numDecodings('226'))
print(s.numDecodings('0'))
print(s.numDecodings('10'))
print(s.numDecodings("1201234"))
print(s.numDecodings("111111111111111111111111111111111111111111111"))
