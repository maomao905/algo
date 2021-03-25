"""
sliding window
keep track of max value in the window
if n < L
    there is any L <= n <= R in the window, it should be included
    add count of window size of last seen L <= n <= R
else if L <= n <= R,
    obviously it should be included
    add count of window size including current n
else if R < n
    we should reset the window size to 0

time O(N) space O(N)
"""
from typing import List
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        N=len(A)
        window_size = 0
        res = [0] * N
        last_max_pos = -1
        for i in range(N):
            if L <= A[i] <= R:
                window_size += 1
                res[i] = window_size
                last_max_pos = i
            elif A[i] < L:
                if last_max_pos >= 0:
                    res[i] = res[last_max_pos]
                window_size += 1
            else:
                window_size = 0
                last_max_pos = -1
        return sum(res)

"""
count subarray size

answer is = number of subarray n <= R - number of subarray only L < n

assuming L < n is 0, L <= n <= R is 1, R < n is 2,
we need to find the window where we have at least one 1 excluding 2
[2,1,0,2,0,0,1,2]
001
01
1
00 <-- this is not valid, we want to substract subarray containing only L < n
"""
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        def count(mx):
            cur = 0
            res = 0
            for n in A:
                if n <= mx:
                    cur += 1
                    res += cur
                else:
                    cur = 0
            return res
        
        N=len(A)
        return count(R) - count(L-1)


s = Solution()
print(s.numSubarrayBoundedMax([2,1,4,3],2,3))
print(s.numSubarrayBoundedMax([2,9,2,5,6],2,8))
print(s.numSubarrayBoundedMax([73,55,36,5,55,14,9,7,72,52],32,69))
