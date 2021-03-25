from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1]-x[0])
        tasks.reverse()
        
        total = tasks[0][1]
        remain = tasks[0][1]
        for actual, minimum in tasks:
            if minimum > remain:
                total += minimum - remain
                remain = minimum
            remain -= actual
        
        return total

s = Solution()
print(s.minimumEffort([[1,2],[2,4],[4,8]]))
print(s.minimumEffort([[1,3],[2,4],[10,11],[10,12],[8,9]]))
print(s.minimumEffort([[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]))
            
