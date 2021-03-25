"""
topological sort
(graph) task -> child tasks
(counter) task -> num of parent tasks (num of dependent tasks)

if counter[x] == 0:
    q.append8(x)

pop x from queue
x is the root task (x has not dependent task, so we can start from here)
decrement counter for x's child tasks (we have done task x, one parent task is now finished)
if counter[task] == 0:
    q.append(task)
    
continue this process until queue becomes empty
if queue is empty and still we have some tasks left, it's not possible to finish all tasks
-> whether length of counter > 0
    
    
time: O(V+E)
V: num of courses
E: num of edges (num of prerequisites)
space: O(V+E)
"""

from typing import List
from collections import defaultdict, Counter, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph = defaultdict(list)
        cnt = Counter()
        
        for child, parent in prerequisites:
            graph[parent].append(child)
            cnt[child] += 1
        
        # get courses which have no parent courses
        sources = [course for course in graph.keys() if course not in cnt]
        
        # done = 0
        q = deque(sources)
        while len(q) > 0:
            course = q.popleft()
            # done += 1
            
            for child in graph[course]:
                cnt[child] -= 1
                if cnt[child] == 0:
                    q.append(child)
                    del cnt[child]
        
        return len(cnt) == 0

s = Solution()
print(s.canFinish(2, [[1,0]]))
print(s.canFinish(2, [[1,0],[0,1]]))
print(s.canFinish(3, [[1,0]]))
print(s.canFinish(3, [[1,0],[2,0]]))
    
        
