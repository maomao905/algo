"""
N: A length, M: B length

brute-force O(NM*min(N,M)) space: O(1)
    iterate A's letter and check if it exists in B one by one and it matches, continue expanding until unmatched

A = [1,2,3,2,1]
B = [3,2,1,4,7]
"""

from typing import List

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        max_cnt = 0
        N, M = len(A), len(B)
        for i in range(N):
            for j in range(M):
                _i = i
                _j = j
                while _i < N and _j < M and A[_i] == B[_j]:
                    _i += 1
                    _j += 1
                
                max_cnt = max(_i-i, max_cnt)
        return max_cnt

"""
(TLE)
binary search O(log(min(N,M)) * (N+M)*min(N,M)) space: O(M^2)
for example, if the max length is in fact, 3, then we never find more than 3 length of common subarray
and we must be able to find less than 3 length of common subarray
 A: [3,2,1] B: [3,2,1] -> A[3,2] B[3,2] must exist

we do binary search and every time, check if the specific length of common subarray exists
how do we check given length k of subarray exists?
    simply take all possible k length of A subarray and store in hash map
    then, we iterate all possible k length of B subarray and check if it matches A's subarray in hash map
time complexity: binary search O(log(min(N,M)))
                 building k-length A's subarray hash map over N-k times O(N-k * k)
                 hashing k-length B's subarray over M-k times O(M-k * k)
                 maximum of k is min(N,M)
space complexity hash map length is O(M) and each size is O(M) -> O(M^2)

"""        
class Solution:
    def check_length(self, A, B, k):
        hs = set()
        for i in range(len(A)-k+1):
            hs.add(tuple(A[i:i+k]))
        
        for j in range(len(B)-k+1):
            if tuple(B[j:j+k]) in hs:
                return True
        return False
        
        
    def findLength(self, A: List[int], B: List[int]) -> int:
        l = 0
        r = min(len(A), len(B))
        
        while l < r:
            mid = l + (r-l) // 2
            if self.check_length(A, B, mid):
                l = mid
            else:
                r = mid-1
        return l

"""
DP O(NM) space: O(NM)
A = [1,2,3,2,1]
B = [3,2,1,4,7]
if A[i] and B[j] matches and common subarray length is k, if A[i+1] and B[j+1] matches, length will be k+1
"""
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        max_len = 0
        dp = [[0] * len(B) for _ in range(len(A))]
        
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    if i < 1 or j < 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                    max_len = max(max_len, dp[i][j])
        
        return max_len

"""
binary search with rabin karp

we can do better when hashing the subarray in the binary search solution
not hashing entire subarray each time, only the first and last element using rabin karp

O(M+N) * log(min(M,N))

A = [1,2,3,2,1]
B = [3,2,1,4,7]
"""
class Solution:
    def check_length(self, A, B, k):
        W = 100
        h = 0
        for i in range(k):
            h = W * h + A[i]
        
        hs = set([h])
        for i in range(len(A)-k):
            h -= A[i] * (W ** (k-1))
            h *= W
            h += A[i+k]
            hs.add(h)
        
        h = 0
        for j in range(k):
            h = W * h + B[j]
        
        if h in hs:
            return True
        
        for j in range(len(B)-k):
            h -= B[i] * (W ** (k-1))
            h *= W
            h += B[i+k]
            if h in hs:
                return True
        return False
        
        
    def findLength(self, A: List[int], B: List[int]) -> int:
        l = 0
        r = min(len(A), len(B))
        
        while l < r:
            mid = l + (r-l) // 2
            if self.check_length(A, B, mid):
                l = mid+1
            else:
                r = mid-1
            # print(mid,l,r)
        return l

s = Solution()
print(s.findLength(A = [1,2,3,2,1], B = [3,2,1,4,7]))
print(s.findLength([0,0,0,0,1],[1,0,0,0,0]))
