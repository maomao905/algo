"""
balanced binary tree
O(logN) per call
"""
from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        # add -INF/INF to the head and the end to make it easy to check leftmost and rightmost boundary
        self.cal = SortedList([(float('-inf'),float('-inf')),(float('inf'),float('inf'))])

    def book(self, start: int, end: int) -> bool:
        interval = (start, end)
        # either bisect(bisect_right)/bisect_left works
        i = self.cal.bisect(interval)
        
        if self.cal[i-1][1] <= start and end <= self.cal[i][0]:
            self.cal.add(interval)
            return True
        
        return False
        


# Your MyCalendar object will be instantiated and called as such:
cal = MyCalendar()
print(cal.book(23,32))
print(cal.book(42,50))
print(cal.book(6,14))
print(cal.book(0,7))
print(cal.book(21,30))
print(cal.book(26,31))
