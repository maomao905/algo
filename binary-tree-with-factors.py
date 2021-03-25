from typing import List
"""
O(N^2)
"""
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        N=len(arr)
        cnt = Counter()
        arr.sort()

        for n in arr:
            cnt[n] += 1
        
        for i in range(N-1):
            for j in range(i+1):
                n = arr[i] * arr[j]
                if n in cnt:
                    cnt[n] += cnt[arr[i]] * cnt[arr[j]] * (2 if arr[i] != arr[j] else 1)
        
        return sum(cnt.values()) % (10**9+7)
                
