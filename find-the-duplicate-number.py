"""
O(1) space
merge sort linked list x

jump to the index of the given value
 0 1 2 3 4
[1,3,4,2,2]

1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2... loop

s f
0 0
1 3
3 4
2 4
4 4

head meeting point
0    4
1    2
3    4
2    2

how to find the loop?
    two pointers (fast and slow)
how to find where the loop starts?
    loop starts at k
    fast and slow meet at m from k
    cycle size is c
    fast loops x times
    
    2(k + m) = k + m + xc
    2k + 2m = k + m + xc
    k = -m + xc
    
    one pointer starts from the head and the other starts from meeting point(m from k)
    then, they will meet where the loop starts
        second pointer moves m - m + xc = xc = 0, which is the entrance of the loop

time: O(N)
    n = k + c
    2(k + m) + k = 3k + 2m
    m < c, 3k + 2m < 3k + 2c < 3k + 3c < 3n < n
space: O(1)
"""

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        first = 0
        second = slow
        
        while first != second:
            first = nums[first]
            second = nums[second]
        
        return first

s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))
print(s.findDuplicate([1,1]))
print(s.findDuplicate([1,1,2]))
