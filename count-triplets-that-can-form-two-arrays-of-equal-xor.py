"""
brute force
O(N^2)
"""
from typing import List
from collections import Counter
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N=len(arr)
        ans = 0
        for j in range(1,N):
            seen = Counter()
            cur = 0
            for i in reversed(range(j)):
                cur ^= arr[i]
                seen[cur] += 1
            
            cur = 0
            for k in range(j,N):
                cur ^= arr[k]
                if cur in seen:
                    ans += seen[cur]
                    print((j,k), seen[cur])
        return ans

"""
prefix xor
if a1^a2^a3 == 0, a1 == a2^a3 or a1^a2 == a3

1. prefix xor to get ai^..aj^..ak == 0
   <-------- prefix xor == 3 ------->
   <--prefix xor == 3-><--xor == 0-->
2. we can split anywhere from i to k (i<j<=k)
   e.g.) current prefix xor is 3, ans += k - seen[3] - 1
3. but the problem is we may have multiple zero xor for each k
    <-------- prefix xor == 3 ------->
    <--xor == 3-><-----xor == 0------>
    <-----xor == 3----><--xor == 0--->
    seen[3] = [1,3]
    for i in seen[3]:
        ans += k - i - 1
    this will be O(N^2) in total
    therefore, keep hashmap of {prefix xor: (total index sum, count of xor)}
    k*count of xor - total index sum - count of xor = (k-1)*count of xor - total index sum
O(N)
"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N=len(arr)
        ans = 0

        seen = {0:(-1,1)} # total index sum, count of xor
        cur = 0
        for k in range(N):
            cur ^= arr[k]
            if cur not in seen:
                seen[cur] = (k, 1)
            else:
                total, cnt = seen[cur]
                res = (k-1)*cnt - total
                ans += res
                seen[cur] = (total+k, cnt+1)
        return ans

s = Solution()
print(s.countTriplets([2,3,1,6,7]))
print(s.countTriplets([1,1,1,1,1]))
print(s.countTriplets([2,3]))
print(s.countTriplets([1,3,5,7,9]))
print(s.countTriplets([7,11,12,9,5,2,7,17,22]))
                    
            
