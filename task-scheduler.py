"""
store the time when the previous task is done
min-heap and if there are same next_available_time, task which hash more remaining tasks is prioritized

[A, A, A, B, B] n = 2

(next_available_time, num_of_tasks, task)

now=0 (0,3,'A'),(0,2,'B')
now=1 (0,2,'B'),(3,2,'A')
now=2 (3,2,'A'),(4,1,'B') -> idle
now=3 (4,1,'B'),(6,1,'A')
now=4 (6,1,'A') -> idle
now=5 (6,1,'A') -> idle
now=6 done

=> it does not work, because in this case [A,B,C,D,E,D,D,D,D,D,D,D] n = 2, D is excecuted first, 
then B,C are executed but D should be executed next, but E is executed because E's time(0) is smaller than D's next avaialble time

"""

from typing import List

# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         heap = [(0, -cnt, task) for task, cnt in Counter(tasks).items()]
#         heapq.heapify(heap)
# 
#         now = 0
#         while len(heap):
#             print(heap)
#             # if the time is available
#             if heap[0][0] <= now:
#                 _, num, task = heapq.heappop(heap)
#                 print(task)
#                 # it's max-heap, so we add up
#                 num += 1
#                 if num < 0:
#                     heapq.heappush(heap, (now+n+1, num, task))
# 
#             now += 1
# 
# 
#         return now

"""
do the most frequent tasks (using heap)
and while waiting for the idle time, do the other less frequent tasks
"""
import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-cnt, task) for task, cnt in Counter(tasks).items()]
        heapq.heapify(heap)
        
        total = 0
        
        while heap:
            # do the most frequent task
            cnt, task = heapq.heappop(heap)
            total += 1
            tmp = []
            k = n
            # do the other tasks while idle
            while k > 0 and heap:
                _cnt, _task = heapq.heappop(heap)
                total += 1
                _cnt += 1
                if _cnt < 0:
                    tmp.append((_cnt, _task))
                k -= 1
            
            for _cnt, _task in tmp:
                heapq.heappush(heap, (_cnt, _task))
            
            cnt += 1
            if cnt < 0:
                heapq.heappush(heap, (cnt, task))
                # if k > 0, idle time still remains, we must wait for k
                total += k
        return total

"""
math
minimum time = when most frequent task ends
AAABBB
most frequent task is A and B
A has 3 tasks, (assume k = 3)
case1 = (k-1) * (n+1) + num_of_most_frequent tasks
A__A__A
 B__B__B

case2 just length of all tasks
e.g.) n = 0
case1 = (3-1) * 1 + 2 = 4
ABABAB -> actually 6

thus, ans = max(case1, case2)

O(N)
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = list(Counter(tasks).values())
        max_freq = max(cnt)
        max_task_num = cnt.count(max_freq)
        
        return max((max_freq-1) * (n+1) + max_task_num, len(tasks))
        
s = Solution()
print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0))
print(s.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))
