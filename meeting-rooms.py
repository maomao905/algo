"""
startでsort O(nlogn)
i
for j in N <--- O(N)
    if jのstart < iのend -> overlap
    if iのend < j start -> break
time: O(NlogN)
space: O(1)
"""

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x[0])
        
        for i in range(len(intervals)):
            if i+1 >= len(intervals):
                return True
            if intervals[i+1][0] < intervals[i][1]:
                return False
        
        return True
            
s = Solution()
print(s.canAttendMeetings([]))
print(s.canAttendMeetings([[0,30],[5,10],[15,20]]))
print(s.canAttendMeetings([[7,10],[2,4]]))
        
        
