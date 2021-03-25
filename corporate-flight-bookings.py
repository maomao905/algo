"""
(TLE)
brute-force
time N^2 in worst
"""
from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for i,j,k in bookings:
            for _i in range(i-1,j):
                res[_i] += k
        return res

"""
cumulative sum
[[1,2,10],[2,3,20],[3,5,25]]
actual
1  2  3  4  5
10 10
   20 20
      25 25 25
10 30 45 25 25 <-- answer

cumulative
(minus means reset the cumulative sum to 0 at the reservation)
1  2  3  4  5
10   -10
   20   -20
      25      -25
10 30 45 25 25 <-- answer
"""
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        _bookings = [0] * n
        for i,j,k in bookings:
            _bookings[i-1] += k
            if j < n:
                _bookings[j] -= k
        
        res = [0] * n
        
        for i in range(n):
            if i == 0:
                res[i] = _bookings[0]
            else:
                res[i] += res[i-1] + _bookings[i]
        return res

s = Solution()
print(s.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]],5))
