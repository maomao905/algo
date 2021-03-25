"""
case studies

1. monotonically increasing
ratings = [1,2,3,4,5]
candies = [1,2,3,4,5]

2. monotonically decreasing
ratings = [5,4,3,2,1]
candies = [5,4,3,2,1]

3.decreasing and then increasing
ratings = [5,4,3,2,1,2,3]
candies = [5,4,3,2,1,2,3]

4.zigzag
ratings = [2,3,4,1,9,5]
candies = [1,2,3,1,2,1]


valley -> 1 candy
peak   -> max(left increasing count, right decreasing count)

O(3N) = O(N)
"""
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        N=len(ratings)
        
        cnt = [1] * N
        # increasing count from head
        for i in range(1,N):
            if ratings[i] > ratings[i-1]:
                cnt[i] = cnt[i-1]+1
        
        cnt_rev = [1] * N
        # increasing count from end
        for i in reversed(range(N-1)):
            if ratings[i] > ratings[i+1]:
                cnt_rev[i] = cnt_rev[i+1]+1
        
        ans = 0
        for i in range(N):
            ans += max(cnt[i], cnt_rev[i])
        return ans

"""
one pass
candy = 3,2,1
ans   = 1,2,3

peak <= down, ans++

      2,3,4,3,2,1
peak    1 2 2 2 2
up      1 2 0 0 0  
down    0 0 1 2 3
ans   1 2 3 1 2 4 <-- why 4, beause peak is not enough if down > peak
truth 1 2 4 3 2 1
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        N=len(ratings)
        peak = up = down = 0
        ans = 1
        for i in range(1,N):
            if ratings[i] > ratings[i-1]:
                up += 1
                down = 0
                peak = up
                ans += up + 1
            elif ratings[i] < ratings[i-1]:
                down += 1
                up = 0
                ans += down + int(peak < down)
            else:
                peak = up = down = 0
                ans += 1
        return ans

s = Solution()
print(s.candy([1,0,2]))
print(s.candy([1,2,2]))
print(s.candy([0,1,2,5,3,2,7]))
print(s.candy([5,3,7,3]))
