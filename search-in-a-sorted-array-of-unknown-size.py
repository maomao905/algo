"""
binary search

if mid is out of range, right = mid - 1
O(log(2^31))
"""
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader:
   def __init__(self, arr):
       self.arr = arr
   def get(self, index: int) -> int:
       if index < len(self.arr):
           return self.arr[index]
       else:
           return 2147483647

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        M = 2147483647
        
        l,r = 0, 10000
        
        while l <= r:
            mid = l + (r-l)//2
            n = reader.get(mid)
            # print((l,mid,r),n)
            if n == target:
                return mid
            elif n == M:
                r = mid-1
            elif n < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

"""
get right boundary first
then binary search
O(log(target))
"""

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        # right boundary should exceed target value
        l,r = 0, 1
        while reader.get(r) < target:
            l = r
            r <<= 1
        
        while l <= r:
            mid = l + (r-l)//2
            n = reader.get(mid)
            
            if n == target:
                return mid
            elif n < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

s = Solution()
arr = [-1,0,3,5,9,12]
r = ArrayReader(arr)
print(s.search(r, 9))
print(s.search(r, 12))
print(s.search(r, -2))
        
        
