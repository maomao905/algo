from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N=len(seats)
        mx = 0
        cur = 0
        
        l,r = seats.index(1), seats[::-1].index(1)
        
        for i in range(l+1,N-r-1):
            if seats[i]:
                cur = 0
            else:
                cur += 1
                mx = max(mx, cur)
        return max(0, (mx+1)//2, l, r)

s = Solution()
print(s.maxDistToClosest(seats = [1,0,0,0,1,0,1]))
print(s.maxDistToClosest(seats = [1,0,0,0]))
print(s.maxDistToClosest(seats = [0,1]))
