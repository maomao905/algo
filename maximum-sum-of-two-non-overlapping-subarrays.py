"""
(WA)
"""

from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        def get_maximum(arr, size):
            cur = 0
            mx = 0
            l,r= 0,0
            for i in range(len(arr)-size+1):
                if i == 0:
                    cur = sum(arr[:size])
                else:
                    cur += arr[i+size-1]
                if cur > mx:
                    l,r = i,i+size-1
                    mx = max(cur, mx)
                cur -= arr[i]
            # print(mx,l,r)
            return mx, l, r
        
        sumL, l, r = get_maximum(A, L)
        sumM1,_,_ = get_maximum(A[:l], M)
        sumM2,_,_ = get_maximum(A[r+1:], M)
        # print(l,r,sumM1,sumM2)
        return sumL + max(sumM1, sumM2)

"""
DP
prefix sum to access subarray (i,j) sum in O(1)

O(N^2)
"""
from itertools import accumulate
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        C = [0] + list(accumulate(A))
        N=len(C)
        memo = {}
        def helper(i,has_L,has_M):
            if i >= N:
                return 0
            if not has_L and not has_M:
                return 0
            
            if (i,has_L,has_M) not in memo:
                mx = 0
                for j in range(i,N):
                    if has_L and j+L >= N:
                        break
                    if has_M and j+M >= N:
                        break
                    
                    if has_L:
                        mx = max(mx, C[j+L] - C[j] + helper(j+L, False, has_M))
                    if has_M:
                        mx = max(mx, C[j+M] - C[j] + helper(j+M, has_L, False))
                memo[i,has_L,has_M] = mx
            return memo[i,has_L,has_M]
    
        return helper(0,True,True)

"""
for i in range(N)
    left max + right max at each split point

O(N)
"""                

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N=len(A)
        
        def max_sum(L,M):
            l_max, r_max = [0] * (N+1), [0] * (N+1)
            l_sum, r_sum = 0, 0
            l,r = 0, N-1
            while l < N:
                l_sum += A[l]
                r_sum += A[r]
                l_max[l+1], r_max[r] = max(l_sum, l_max[l]), max(r_sum, r_max[r+1])
                if l+1 >= L:
                    l_sum -= A[l-L+1]
                if l+1 >= M:
                    r_sum -= A[r+M-1]
                l += 1
                r -= 1
            
            res = 0
            for i in range(N):
                res = max(res, l_max[i] + r_max[i])
            return res
        
        return max(max_sum(L,M), max_sum(M,L))

"""
fix L subarray
                       i
<--max of M (prefix)--><-- L --><--max of M (suffix)-->

assuming l_max[i] is max of L subarray starting i th index
l_max[i] = max(max of M (prefix), max of M (suffix))

1. max of M subarray up to ith index (ending at ith index)
[0,6,5,2,2,5,1,9,4] L=1, M=2
m_prefix_max = [None,6,11,11,11,11,11,13]
2. max of M subarray from ith index (starting ith index)
m_suffix_max = [13,13,13,13,13,13,13,None]

3. fix L subarray and find max M subarray prefix and suffix
for i in range(N):
    A[i] + max(m_prefix_max[i-1], m_suffix_max[i+1])
"""
from typing import List
from itertools import accumulate
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N=len(A)
        C = [0] + list(accumulate(A))
        M_prefix_max = [0] * N
        M_suffix_max = [0] * N
        
        # 1. max of M subarray up to ith index (ending at ith index)
        for i in range(M-1,N):
            if i == M-1:
                M_prefix_max[i] = C[i+1] - C[i-M+1]
            else:
                M_prefix_max[i] = max(C[i+1] - C[i-M+1], M_prefix_max[i-1])
        
        # 2. max of M subarray from ith index (starting ith index)
        for i in reversed(range(N-M+1)):
            max_so_far = 0 if i+1 == N else M_suffix_max[i+1]
            M_suffix_max[i] = max(C[i+M] - C[i], max_so_far)
        
        # 3. fix L subarray and find max M subarray prefix and suffix
        ans = 0
        for i in range(N-L+1):
            l_sum = 0
            if i == 0:
                l_sum = C[i+L]
            else:
                l_sum = C[i+L] - C[i]
            
            prefix = M_prefix_max[i-1] if i > 0 else 0
            suffix = M_suffix_max[i+L] if i+L<N else 0
            ans = max(ans, l_sum + max(prefix, suffix))
        return ans
        
s = Solution()
print(s.maxSumTwoNoOverlap(A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2))
print(s.maxSumTwoNoOverlap(A = [3,8,1,3,2,1,8,9,0], L=3,M=2))
print(s.maxSumTwoNoOverlap(A = [2,1,5,6,0,9,5,0,3,8], L=4,M=3))
print(s.maxSumTwoNoOverlap(A = [1,1,5,6,0,9,5,0,1,1], L=4,M=3))
                    
                
