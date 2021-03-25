# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
from itertools import accumulate
class ArrayReader(object):
    def __init__(self, arr):
        self.arr = list(accumulate(arr))
    
    def __get_sum(self, l,r):
        if l == 0:
            return self.arr[r]
        return self.arr[r] - self.arr[l-1]
        
    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        s1, s2 = self.__get_sum(l,r), self.__get_sum(x,y)
        if s1 > s2:
            return 1
        elif s1 < s2:
            return -1
        else:
            return 0

    def length(self) -> int:
        return len(self.arr)

"""
binary search
"""
class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        N=reader.length()
        l,r=0,N-1
        
        while l < r:
            mid = l + (r-l)//2
            r_mid = mid + 1
            if (r-l) % 2 == 0:
                r_mid = mid
            res = reader.compareSub(l,mid,r_mid,r)
            if res == 1:
                r = mid
            elif res == -1:
                l = mid+1
            else:
                return mid
        return l
            
r = ArrayReader([7,7,7,7,10,7,7,7])
s = Solution()
print(s.getIndex(r))
r = ArrayReader([6,6,12])
print(s.getIndex(r))
