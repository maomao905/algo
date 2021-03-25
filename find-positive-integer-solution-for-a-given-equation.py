"""
binary search

O(XlogY)
"""
from typing import List
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
  
"""
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x * y

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        def bsearch(x):
            l,r = 1,1000
            while l<r:
                mid = (l+r)//2
                res = customfunction.f(x,mid)
                if res == z:
                    return mid
                elif res < z:
                    l = mid+1
                else:
                    r = mid-1
            return l
            
        ans = []
        # fix x and calculate y
        for x in range(1,1001):
            y = bsearch(x)
            if customfunction.f(x,y) == z:
                ans.append([x,y])
        return ans

"""
matrix search
- reduct search space row/column one by one
if mat[i][j] > z: mat[i+1][j] (go down)
if mat[i][j] < z: mat[i][j-1] (go left)
if mat[i][j] == z: mat[i-1][j-1] (go left and down)

1 2 3 4 5
2 3 4 5 6
3 4 6 7 8
4 5 6 7 10
5 7 9 11 12

O(X+Y)
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        x,y = 1,1000
        
        while 1<=x<=1000 and 1<=y<=1000:
            res = customfunction.f(x,y)
            if res < z:
                x += 1
            elif res > z:
                y -= 1
            else:
                ans.append([x,y])
                x += 1
                y -= 1
                
        return ans

"""
optimized binary search
      
      possible y
x= 1, 1 2 3 4 5 6  -> if binary search returns 3 and f(x,y)==z
x=2,  1 2          -> possible y is only 1 or 2, y < 3 since f(x,y)<f(x+1,y)

loop X time and search time is logY + log(Y-1) + log(Y-2) .... 1
O(XlogY)
"""        

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        def bsearch(x,r):
            l=1
            while l<r:
                mid = (l+r)//2
                res = customfunction.f(x,mid)
                if res == z:
                    return mid
                elif res < z:
                    l = mid+1
                else:
                    r = mid-1
            return l
            
        ans = []
        r=1000
        # fix x and calculate y
        for x in range(1,1001):
            y = bsearch(x,r)
            if customfunction.f(x,y) == z:
                ans.append([x,y])
            r = y
        return ans

customfunction = CustomFunction()
s = Solution()
print(s.findSolution(customfunction, 5))
