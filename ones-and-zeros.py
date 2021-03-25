"""
(WA)
{'10', '0001', '1', '0'} 0 x 5times (m) and 1 x 3times (n)

divide the cases
m = 5
if we know maximum subset size, when m = 4, choosing the 0 appear only once

smallest subproblems
0's occurence
dp[0] = 0
dp[1] = 1 {10}, {0}
dp[2] = 2 {10, 0}, {111001}
dp[3] = 2 {0001}, {10, 111001}, {0, 111001}
dp[4] = 3 {0001, 10}, {0001, 0}, {111001, 10, 0}
dp[5] = 3 {10, 0001, 0}, {111001, 0001}

dp[i] -> dp[i-1] if there is a string that contains 0 at one time, dp[i-1] + 1
dp[i] -> dp[i-2] if there is a string that contains 0 at two times, dp[i-2] + 1
we don't know dp[i-1] is greater than dp[i-2]

we make hash map 
{number of 0 occurence: [index]}

where is the independent point?
"""

from typing import List
from collections import defaultdict, Counter

# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         cnt_zero = defaultdict(list)
#         cnt_one = defaultdict(list)
#         for i, s in enumerate(strs):
#             cnt = Counter(s)
#             if cnt.get('0', 0) > m or cnt.get('1', 0) > n:
#                 continue
# 
#             cnt_zero[cnt.get('0', 0)].append(i)
#             cnt_one[cnt.get('1', 0)].append(i)
# 
#         dp = [[0] * (n+1) for _ in range(m+1)]
# 
#         for i in range(m):
#             for j in range(n):
#                 for _j in reversed(j):
#                     dp[i][j] = dp[i][_j] + dp[i][j-_j]
        

"""
(TLE)
brute-force

generate all possible subsets of strs and check count of 0 and 1 matches the m and n
O(2^N * NL) L is string size and NL for taking count of 0 and 1
"""

class Solution:
    def findMaxForm(self, strs, m, n):
        def count_zero_ones(strs):
            zero = 0
            one = 0
            for s in strs:
                cnt = Counter(s)
                zero += cnt.get('0', 0)
                one += cnt.get('1', 0)
            return zero, one
        
        def recursive(i, comb=[]):
            if i >= len(strs):
                cnt_zero, cnt_one = count_zero_ones(comb)
                if cnt_zero == m and cnt_one == n:
                    # print(comb)
                    nonlocal max_size
                    max_size = max(max_size, len(comb))
                return
            comb.append(strs[i])
            recursive(i+1, comb)
            comb.pop()
            recursive(i+1, comb)
        max_size = 0
        recursive(0)
        return max_size

"""
(TLE)
better brute-force

try all possible subsets of strs but we don't have to generate subsets but only keep the zero/ones count
if counts exeeds m/n, we stop recursion

O(2^N + NL) L is string size and for taking count of 0 and 1
"""

class Solution:
    def findMaxForm(self, strs, m, n):
        def count_zero_ones(s):
            if s in hm:
                return hm[s][0], hm[s][1]
            cnt = Counter(s)
            c = (cnt.get('0', 0), cnt.get('1', 0))
            hm[s] = c
            return c[0], c[1]
        
        def recursive(i, cnt_zero=0, cnt_one=0, size=0):
            if i >= len(strs):
                if cnt_zero == m and cnt_one == n:
                    nonlocal max_size
                    max_size = max(max_size, size)
                return
            
            # skip i
            recursive(i+1, cnt_zero, cnt_one, size)
            
            # include i
            zero, one = count_zero_ones(strs[i])
            cnt_zero += zero
            cnt_one += one
            if cnt_zero > m or cnt_one > n:
                return
            recursive(i+1, cnt_zero, cnt_one, size+1)
        
        hm = {}
        max_size = 0
        recursive(0)
        return max_size

"""
memorization
there are some overlap, we can memorize them
[a,d,e]
[b,d,e]  d,e are overlapped

when we choose one of strs, remaining m/n will be reduce.
recursive(i, m, n)
    if i == end of strs:
        return m == 0 and n == 0
    
    if (i, m, n) in memo:
        return memo[(i,m,n)]
    
    r1 = recursive(i+1, m, n)
    zeros, ones = get count of strs[i]
    r2 = recursive(i+1, m-zeros, n-ones)
    
    memo[(i, m, n)] = r1 or r2 # save result

time and space: O(S*m*n) same as size of memo 
"""

from functools import lru_cache
class Solution:
    def findMaxForm(self, strs, m, n):
        @lru_cache(maxsize=None)
        def count_zero_ones(s):
            cnt = Counter(s)
            return cnt.get('0', 0), cnt.get('1', 0)
        
        def recursive(i, m, n):
            if i >= len(strs):
                return 0
            
            key = (i, m, n)
            cache = memo.get(key)
            if cache:
                return cache
            
            # skip i
            r1 = recursive(i+1, m, n)
            
            # include i
            zero, one = count_zero_ones(strs[i])
            m -= zero
            n -= one
            r2 = 0
            if m >= 0 and n >= 0:
                r2 = recursive(i+1, m, n) + 1
            
            r = max(r1, r2)
            memo[key] = r
            return r
            
        memo = {}
        return recursive(0, m, n)

"""
DP
3 dimentions
time and space: O(S*N*M)
"""

class Solution:
    def findMaxForm(self, strs, m, n):
        def count_zero_ones(s):
            cnt = Counter(s)
            return cnt.get('0', 0), cnt.get('1', 0)
        
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
        
        for i in range(1, len(strs)+1):
            zeros, ones = count_zero_ones(strs[i-1])
            for j in range(m+1):
                for k in range(n+1):
                    if j-zeros >= 0 and k-ones >= 0:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zeros][k-ones]+1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        return dp[-1][-1][-1]

"""
DP
for s in strs
    zeros, ones = count_zero_ones(s)
    for i in reverse(m)
        for j in reverse(n)
            # dp[i][j] size of subset using i of 0s and j of 1s
            dp[i][j] = max(dp[i][j], 1 + dp[i-zeros][j-ones])
    return dp[-1][-1]
why we go backbard?
    - prevent overwriting previous state
time: O(S*M*N)
space: O(MN)
"""
class Solution:
    def findMaxForm(self, strs, m, n):
        def count_zero_ones(s):
            cnt = Counter(s)
            return cnt.get('0', 0), cnt.get('1', 0)
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            zeros, ones = count_zero_ones(s)
            
            for i in reversed(range(zeros, m+1)):
                for j in reversed(range(ones, n+1)):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-zeros][j-ones])
        
        return dp[-1][-1]


s = Solution()
print(s.findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))
print(s.findMaxForm(strs = ["10","0","1"], m = 1, n = 1))
print(s.findMaxForm(strs = ["0","0","1","1"], m = 2, n = 2))
print(s.findMaxForm(["10","0001","111001","1","0"],3,4))
