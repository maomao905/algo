from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = [int(s[:2]) * 60 + int(s[3:]) for s in timePoints]
        
        time.sort()
        
        # difference between the start and the end
        ans = float('inf')
        N=len(time)
        for i in range(N):
            if i == 0:
                ans = time[0] + 24*60 - time[-1]
            else:
                ans = min(ans, time[i]-time[i-1])
        return ans

s = Solution()
print(s.findMinDifference(["23:59", '00:00']))
print(s.findMinDifference(['00:00', "23:59", '00:00']))
        
        
