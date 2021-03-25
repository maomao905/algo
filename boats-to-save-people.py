"""
picking always minimum weight does not work
[3,8,7,1,4] limit=9
incorrect [1,3][4][7][8] -> 4
expected  [3,4][1,7][8] -> 3

greedy
we want to make best use of limit at each boat
sort [1,3,4,7,8]
two pointers from start and end
pick [1,8] remain [3,4,7] possible to sum people[l] + people[r] <= limit
pick [7] remain [3,4] impossible, use a boat for rightmost people
pick [3,4]

x,y,z
l   r if l+=1 and r-=1 and l, r are at y (l==r), need to carry y at the end
l r   if r-=1 and r is at y
l r   if l+=1 and r-=1, l > r and we carried all
l r   if r-=1, l == r and we need to carry l at the end

time O(NlogN) space O(1)
"""
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N=len(people)
        people.sort()
        ans = 0
        l,r = 0,N-1
        
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
            ans += 1
            r -= 1
        
        if l == r:
            ans += 1
        
        return ans
            
s = Solution()
print(s.numRescueBoats([1,2], 3))
print(s.numRescueBoats([3,2,2,1], 3))
print(s.numRescueBoats([3,5,3,4], 5))
print(s.numRescueBoats([3,8,7,1,4], 9))
