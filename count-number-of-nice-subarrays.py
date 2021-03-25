"""
sliding window
we always want to take the maximum window size
[2,2,2,1,2,2,1,2,2,2]
<----- window ----->
<---->         <---->
4choices  x    4choices = 16, which is the answer

expand the window as long as the condition is satisfied
when the window is invalid, shrink the window until window becomes valid again

in order to know how many choices we have in left and right
we keep leftmost and rightmost odd number in the window

time O(N) space O(1)
"""
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        l_odd = len(nums)
        for r, n in enumerate(nums):
            if n % 2:
                l_odd = min(l_odd, r)
                k -= 1
            
            if k == 0:
                ans += l_odd - l + 1
            
            i = l_odd + 1
            while k < 0:
                if nums[i] % 2:
                    l = l_odd + 1
                    l_odd = i
                    ans += l_odd - l + 1
                    # print(l, l_odd)
                    k += 1
                    break
                i += 1
        return ans

"""
deque

keep k+1 odd nums in queue

[2,2,2,1,2,2,2,1,2,2,2,2,2,2,1,2,2] k=2
        <-add-><---window--->
     q[0]    q[1]         q[2]
q[1]-q[0] is the available choices when r == third 1
"""
from collections import deque
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        q = deque([-1])
        ans = 0
        for i, n in enumerate(nums):
            if n % 2:
                q.append(i)
            if len(q) > k+1:
                q.popleft()
            if len(q) == k + 1:
                ans += q[1] - q[0]
        return ans

s = Solution()
print(s.numberOfSubarrays([1,1,2,1,1],3))
print(s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2],2))
print(s.numberOfSubarrays([2044,96397,50143],1))
print(s.numberOfSubarrays(
[1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1],4))
            
