"""
overlap condition
overlap x axis and overlap y axis

how to know it's overlapping

case1: <--a--> <--b--> non-overlapping
case2: <--a--><--b-->  non-overlapping
case3: <--a-->         overlapping
          <--b-->
case4: <--a-->         overlapping
        <-b->
"""
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def overlap(x1,x2):
            a = max(max(x1), max(x2)) - min(min(x1), min(x2))
            b = abs(x1[0]-x1[1]) + abs(x2[0]-x2[1])
            return a < b
        
        x = overlap((rec1[0],rec1[2]),(rec2[0],rec2[2]))
        y = overlap((rec1[1],rec1[3]),(rec2[1],rec2[3]))
        
        return x and y

        
