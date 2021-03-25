"""
how many overlaps exist at one time most?
when overlap?
start1 < start2 and end1 > end2

sort by start time

time: O(N^2)
space: O(N)
"""
# class Solution(object):
#     def minMeetingRooms(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: int
#         """
#         # sort by start time
#         intervals.sort(key=lambda x: x[0])
# 
#         max_overlap = 0
#         overlap_meetings = []
#         for start, end in intervals:
#             overlap_meetings = [(_start, _end) for _start, _end in overlap_meetings if _end > start]
#             overlap_meetings.append((start, end))
#             max_overlap = max(max_overlap, len(overlap_meetings))
# 
#         return max_overlap

"""
min heap
end timeをheapに保存
heapに保存されているintervalは必ずstart timeが古いので
heapのtopのend timeがstart timeを超えていれば、必ず新たにmeeting roomが必要

time: sort O(NlogN) for sort + O(N*logN) for push/pop -> O(NlogN)
space: O(N) in worst case
"""
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort by start time
        intervals.sort(key=lambda x: x[0])
        
        if len(intervals) == 0:
            return 0
        
        min_heap = [intervals[0][1]]
        
        for start, end in intervals[1:]:
            if start >= min_heap[0]:
                heapq.heappop(min_heap)
        
            heapq.heappush(min_heap, end)
        
        return len(min_heap)

s = Solution()
print(s.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print(s.minMeetingRooms([[7, 10],[2, 4]]))
print(s.minMeetingRooms([[1,5],[8,9],[8,9]]))
                
            
