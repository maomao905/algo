"""
[1,2,3,4,5,6,7,8]


1. brute-force O(2^N)
choosing the all subsequence and check if it's fibonacci

2. fix two pairs and expading as much as it can
if we know two pairs, there is only single path
1,2 are fixed, 1,2,3,5,8...
3,10 are fixed, 3,10,13,23,36

try all possible fix two pairs and update maximum length of fibonacci
how to find two sum exists? -> hash set

time: O(nC2 * n) -> nC2 = N^2 and if M is maximum of array, logM
2 4 8 16.. even if you multiply previous element by 2, logM
space: O(N)
"""
from typing import List

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        hs = set(A)
        
        N=len(A)
        
        max_cnt = 0
        for i in range(N):
            for j in range(i+1,N):
                x, y = min(A[i], A[j]), max(A[i], A[j])
                
                cnt = 2
                while x + y in hs:
                    cnt += 1
                    # print(cnt, x, y, x+y)
                    x, y = y, x + y
                
                max_cnt = max(cnt, max_cnt)
        
        return max_cnt if max_cnt >= 3 else 0

"""
3. DP
[1,3,7,11,12]

if last two(or three including current) are decided, it must be fibonacci.
1 -> 2 -> 3 -> 5 -> 8
which means how many fibonacci we have before the three does not matter.

if dp[i][j] is the number of fibonacci up to jth index and last two are ith and jth index
and if arr[i] + arr[j] = arr[k], dp[j][k] = dp[i][j] + 1
-> how do we know ith index
use hash map of {value: index} and if given arr[j] and arr[k], arr[i] is determined

row is start index and column is end index

 0 1 2 3  4  5  6
[1,3,7,11,12,14,18] row(i) is last fibonacci and col(j) is current fibonacci:
   0 1 2 3 4 5 6
0  x 2 2 2 2 2 2
1    x 2 2 2 2 2
2      x 2 2 2 2
3        x 3 3 3 -> longest length is 3
4          x 2 2
5            x 2
6              x

time ans space: O(N^2)
"""

class Solution:
    def lenLongestFibSubseq(self, A):
        N=len(A)
        val_to_idx = {A[i]: i for i in range(N)}
        
        dp = [[2]*N for _ in range(N)]
        max_length = 2
        for j in range(N):
            for k in range(j+1,N):
                i_val = A[k]-A[j]
                if i_val not in val_to_idx:
                    continue
                i = val_to_idx[i_val]
                if i < j:
                    dp[j][k] = dp[i][j] + 1
                    max_length = max(max_length, dp[j][k])
        
        return max_length if max_length > 2 else 0
        
s = Solution()
print(s.lenLongestFibSubseq([1,2,3,4,5]))
print(s.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(s.lenLongestFibSubseq([1,3,7,11,12,14,18]))
print(s.lenLongestFibSubseq([1,2,5]))
