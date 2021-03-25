"""
(WA)
24,2452
242452 < 245224, because 24(24) < 2452

nums = [3,30,34,5,9]
max(nums) = 34
digit of max number = 2
"""

from typing import List
import math
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        m = max(nums)
        if m == 0:
            return 0
        
        d = int(math.log10(m)) + 1
        
        nums2 = [None] * len(nums)
        
        for i in range(len(nums)):
            s = str(nums[i])
            if len(s) < d:
                nums2[i] = (int(s * (d // len(s)) + s[:(d % len(s))])-1, i)
            else:
                nums2[i] = (nums[i], i)
        
        nums2.sort(key=lambda x: x[0], reverse=True)
        # print(nums2)
        
        res = []
        for _, i in nums2:
            res.append(str(nums[i]))
        
        return ''.join(res)

"""
comparator x+y>y+x

23234,234
23423234 > 23234234 
-> we can compare by concatnating the int in both way
-> make the custom comparator

time: O(NlogN) NlogN for sort, and comparator takes constant time
space: O(N)
"""

class CustomComparator(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums):
        res = ''.join(sorted(map(str,nums), key=CustomComparator))
        return '0' if res[0] == '0' else res

s = Solution()        
print(s.largestNumber([10,2]))
print(s.largestNumber([3,30,34,5,9]))
print(s.largestNumber([1]))
print(s.largestNumber([10]))
print(s.largestNumber([23234,234,23]))
print(s.largestNumber([432,43243]))
print(s.largestNumber([0,0]))
