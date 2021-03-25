from typing import List
"""
brute-force
O(N^2)
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        N=len(rating)
        for i in range(N):
            smaller_count = 0
            for j in range(i):
                if rating[i] > rating[j]:
                    smaller_count += 1
            
            larger_count = 0
            for j in range(i+1,N):
                if rating[i] < rating[j]:
                    larger_count += 1
            
            ans += smaller_count * larger_count + (i-smaller_count) * (N-i-1-larger_count)
        return ans

"""
O(NlogN) using binary tree
"""
from sortedcontainers import SortedList
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        N=len(rating)
        smaller = [0] * N
        larger = [0] * N
        
        sl = SortedList()
        for i in range(N):
            sl.add(rating[i])
            j = sl.index(rating[i])
            smaller[i] = j
        
        sl = SortedList()
        for i in reversed(range(N)):
            sl.add(rating[i])
            j = sl.index(rating[i])
            larger[i] = len(sl)-j-1
        
        for i in range(N):
            ans += smaller[i] * larger[i] + (i-smaller[i]) * (N-i-1-larger[i])
        return ans
        
s = Solution()
print(s.numTeams([2,5,3,4,1]))
print(s.numTeams([2,1,3]))
print(s.numTeams([1,2,3,4]))
