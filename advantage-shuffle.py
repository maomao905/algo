"""
O(NlogN)
"""
from typing import List
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        N=len(A)
        A.sort()
        B = sorted([(n, i) for i, n in enumerate(B)])
        
        res = [0] * N
        j = 0
        for i in range(N):
            a, b = A[i], B[i]
            if a > b[0]:
                res[b[1]] = a
                j += 1
            else:
                while j < N and A[i] <= b[0]:
                    A[i], A[j] = A[j], A[i]
                    j += 1
                res[b[1]] = A[i]
        return res

"""
sort and allocate greater element for each b
O(NlogN)
"""
from collections import defaultdict
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        N=len(A)
        A.sort()
        res = defaultdict(list)
        for b in sorted(B)[::-1]:
            if A[-1] > b:
                res[b].append(A.pop())
        return [(res[b] or A).pop() for b in B]

"""
balanced binary tree
if A[i] > B[i] exists, we want to use smallest larger value for A[i] than B[i],
else pick up from smallest value

store A in balanced binary tree
for b in B:
    find smallest larger value than b
    if exist:
        store it in result and delete it from A
    else:
        choose the smallest one from A and delete it

O(NlogN)
"""
from sortedcontainers import SortedList
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = SortedList(A)
        res = []
        for b in B:
            i = A.bisect_right(b)
            if i >= len(A):
                res.append(A.pop(0))
            else:
                res.append(A.pop(i))
        return res
        
s = Solution()
print(s.advantageCount([2,7,11,15],[1,10,4,11]))
print(s.advantageCount([12,24,8,32],[13,25,32,11]))
