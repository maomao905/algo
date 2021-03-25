"""
abs(arr1[i]-arr1[j]) + abs(arr2[i]-arr2[j]) + (i-j)

if arr1[i] > arr1[j]
    arr1[i] - arr1[j]
else
    arr1[j] - arr1[i]

if arr2[i] > arr2[j]
    arr2[i] - arr2[j]
else
    arr2[j] - arr2[i]

4 possibilities
(arr1[i] - arr1[j]) + (arr2[i] - arr2[j]) -> max(arr1[i] + arr2[i]) - min(arr1[j] + arr2[j])
(arr1[i] - arr1[j]) + (arr2[j] - arr2[i]) -> max(arr1[i] - arr2[i]) - min(arr[j] - arr2[j])
(arr1[j] - arr1[i]) + (arr2[i] - arr2[j]) -> max(-arr1[i] + arr2[i]) - min(-arr1[j] + arr2[j])
(arr1[j] - arr1[i]) + (arr2[j] - arr2[i]) -> max(-arr1[i] - arr2[i]) - min(-arr1[j] - arr2[j])

"""
from typing import List
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        N=len(arr1)
        arr = [[0]*N for _ in range(8)]
        for i in range(N):
            arr[0][i] = arr1[i] + arr2[i] + i
            arr[1][i] = arr1[i] + arr2[i] - i
            arr[2][i] = arr1[i] - arr2[i] + i
            arr[3][i] = arr1[i] - arr2[i] - i
            arr[4][i] = -arr1[i] + arr2[i] + i
            arr[5][i] = -arr1[i] + arr2[i] - i
            arr[6][i] = -arr1[i] - arr2[i] + i
            arr[7][i] = -arr1[i] - arr2[i] - i
        
        # print(arr)
        
        ans = float('-inf')
        for i in range(8):
            _max = float('-inf') 
            _min = float('inf') 
            for j in range(N):
                _max = max(_max, arr[i][j])
                _min = min(_min, arr[i][j])
                # print(_max, _min, j)
            # print(_max, _min)
            ans = max(ans, _max-_min)
        
        return ans

"""
4 possibilities
(arr1[i] - arr1[j]) + (arr2[i] - arr2[j]) -> max(arr1[i] + arr2[i]) - min(arr1[j] + arr2[j])
(arr1[i] - arr1[j]) + (arr2[j] - arr2[i]) -> max(arr1[i] - arr2[i]) - min(arr1[j] - arr2[j])
(arr1[j] - arr1[i]) + (arr2[i] - arr2[j]) -> max(-arr1[i] + arr2[i]) - min(-arr1[j] + arr2[j])
(arr1[j] - arr1[i]) + (arr2[j] - arr2[i]) -> max(-arr1[i] - arr2[i]) - min(-arr1[j] - arr2[j])

f(i) = x * arr1[i] + y * arr2[i] + i where (x, y) = ((1,1),(1,-1),(-1,1),(-1,-1))
answer = max(f(i)) - min(f(j))

Manhattan distance
maximum distance from any two points can be calculated by 
set 4 points and answer is max(max(distance) - min(distance))
x      x

x      x
"""
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        N=len(arr1)
        cal = lambda x, y, i: x * arr1[i] + y * arr2[i] + i
        
        ans = float('-inf')
        for x, y in ((1,1),(1,-1),(-1,1),(-1,-1)):
            mi, mx = float('inf'), float('-inf')
            for i in range(N):
                d = cal(x, y, i)
                mx = max(mx, d)
                mi = min(mi, d)
            ans = max(ans, mx-mi)
        return ans
        

s = Solution()
print(s.maxAbsValExpr([1,2,3,4],[-1,4,5,6]))
print(s.maxAbsValExpr(arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]))
