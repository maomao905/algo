from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N=len(arr)
        cur = 1
        ans = 1
        for i in range(1,N):
            if i > 1 and arr[i-2] < arr[i-1] and arr[i-1] > arr[i]:
                cur += 1
            elif i > 1 and arr[i-2] > arr[i-1] and arr[i-1] < arr[i]:
                cur += 1
            else:
                cur = 1 if arr[i-1] == arr[i] else 2
            ans = max(cur, ans)
        return ans

s = Solution()
print(s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
print(s.maxTurbulenceSize([4,8,12,16]))
print(s.maxTurbulenceSize([100]))
print(s.maxTurbulenceSize([9,9]))
print(s.maxTurbulenceSize([9,8]))
