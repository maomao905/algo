"""
(WA)
binary search

in case of [2,4,1,3] does not work at width 2 but width 3 works, which means binary search does not work
O(NlogN)
"""
from typing import List
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        N=len(A)
        def is_valid(width):
            for i in range(N-width):
                if A[i] <= A[i+width]:
                    return True
            return False
        
        l,r = 0,N-1
        while l<r:
            mid = (l+r)//2 + (r-l)%2
            if is_valid(mid):
                l = mid
            else:
                r = mid-1
        return l

"""
1. fix i and iterate N times O(N)
2. at each iteration, find farest j where A[j] is larger than A[i]
    if j1 < j2 and A[j1] <= A[j2], choose j2
    [6,0,8,2,1,5]
    [8,8,8,5,5,5] prepare decreasing array
3. binary search to find the closest larger index j

O(NlogN)
"""
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        def search(i):
            l,r = i+1,N-1
            while l < r:
                mid = (l+r)//2 + (r-l)%2
                if arr[mid] >= A[i]:
                    l = mid
                else:
                    r = mid - 1
            return l
        
        N=len(A)
        arr = [A[-1]] * N # keep larger farest value
        for i in reversed(range(N-1)):
            if arr[i+1] < A[i]:
                arr[i] = A[i]
            else:
                arr[i] = arr[i+1]
        
        ans = 0
        for i in range(N-1):
            j = search(i)
            if A[j] >= A[i]:
                ans = max(ans, j-i)
            
        return ans

"""
stack
1. keep i candidates (decreasing stack)
    if we find smaller value, keep the index
2. iterate from the end and if it's bigger than value in stack, it's valid pair so update the answer

O(N)
"""
class Solution:
    def maxWidthRamp(self, A):
        N=len(A)
        small = []
        for i in range(N):
            if not small or A[i]<A[small[-1]]:
                small.append(i)
        
        ans = 0
        for j in reversed(range(N)):
            while small and A[small[-1]] <= A[j]:
                ans = max(ans, j-small.pop())
        return ans
            
        
s = Solution()
print(s.maxWidthRamp([6,0,8,2,1,5]))
print(s.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))
print(s.maxWidthRamp([2,4,1,3]))
print(s.maxWidthRamp([1,0]))
print(s.maxWidthRamp([0,1]))
