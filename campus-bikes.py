"""
N workers, M bikes N <= M
assign bike to worker with shortest Manhattan distance between them
repeat this process until there are no available workers

ans = [bike_index, ....] size is number of workers

time: O(MN) + O(N*MlogM) + O(N) + O(NlogN) + O(NMlogN)
    = O(N*MlogM) + O(NMlogN)
    = O(NM (logM + logN))
    = O(NM log(NM))
space: O(MN) + O(N) + O(M) -> O(MN)

in brute-force apprach
calculate distance matrix O(MN)
sort the all the distance matrix elements O(MNlogMN)
assign bikes to all workers O(MN)
time: O(MNlogMN)
  -> it is actually same as normal sort of entire distance matrix elements
"""
from typing import List
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        
        # final answer is pair of worker index and bike index
        # we need to sort the distance as well
        # thus, we keep the both index in sorted distance matrix
        # row is worker and each row has sorted distance between the worker and the bike
        # time: O(MN) + O(N * MlogM) for sort
        # space: O(MN)
        for i, (x_w, y_w) in enumerate(workers):
            distances.append([])
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x_w - x_b) + abs(y_w - y_b)
                distance[-1].append((distance, i, j))
            distances[-1].sort(reverse=True)
        
        # smallest distance for each worker
        # heap size is always N
        # O(N) for creating list + O(NlogN) for heapify
        heap = [distances[i].pop() for i in range(len(workers))]
        heapq.heapify(heap)
        
        result = [None] * len(workers)
        used_bikes = set()
        
        # until assign bikes to all workers
        # O(NM) loop in worst * O(logN) for heap pop and push
        # O(NM) loop because all bikes are already used for each worker 
        while len(used_bikes) < len(workers):
            # pop shortest distance pair
            _, worker, bike = heapq.heappop(heap)
            if bike not in used_bikes:
                result[worker] = bike
                used_bikes.add(bike)
            else:
                # add next shortest distance pair for the worker
                # because bike is already used and we have to find another bike
                heapq.heappush(heap, distances[worker].pop())
"""
stable marriage problem = matching between workers and bikes problem
1. each worker submit closest bike
2. if closest bike is already taken, compare the distance and if it is closer, take it
    and rejected worker goes next round
3. until all worker get bike, rejected workers continue to choose next closer bike

time: O(N * MlogM) for sort + O(N^2) for selection -> O(NMlogM)
space: O(MN)
"""
from collections import deque
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        
        # final answer is pair of worker index and bike index
        # we need to sort the distance as well
        # thus, we keep the both index in sorted distance matrix
        # row is worker and each row has sorted distance between the worker and the bike
        # time: O(MN) + O(N * MlogM) for sort
        # space: O(MN)
        for i, (x_w, y_w) in enumerate(workers):
            distances.append([])
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x_w - x_b) + abs(y_w - y_b)
                distances[-1].append((distance, i, j))
            distances[-1].sort(reverse=True)
        
        result = [None] * len(workers)
        used_bikes = [None] * len(bikes)
        
        # O(N^2)
        q = deque([i for i in range(len(workers))])
        while len(q) > 0:
            w_i = q.popleft()
            
            dist, _, b_i = distances[w_i].pop()
            
            if used_bikes[b_i]:
                old_dist, old_w_i = used_bikes[b_i]
                if dist < old_dist:
                    used_bikes[b_i] = (dist, w_i)
                    result[w_i] = b_i
                    q.append(old_w_i)
                else:
                    q.append(w_i)
            else:
                result[w_i] = b_i
                used_bikes[b_i] = (dist, w_i)
        
        return result

"""
bucket sort
distance range is [0, 2000] 1000+1000 = 2000
all pairs of worker and bike are put into bucket
and just iterate to get answer
time and space: O(MN)
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        buckets = [[] for _ in range(2000)]
        distances = []
        
        # O(MN)
        for i, (x_w, y_w) in enumerate(workers):
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x_w - x_b) + abs(y_w - y_b)
                buckets[distance].append((i, j))
        
        result = [None] * len(workers)
        used_bikes = [False] * len(bikes)
        # O(MN)
        for bucket in buckets:
            for w_i, b_i in bucket:
                if result[w_i] is None and not used_bikes[b_i]:
                    result[w_i] = b_i
                    used_bikes[b_i] = True
        
        return result


s = Solution()
workers = [[0,0],[2,1]]; bikes = [[1,2],[3,3]]
print(s.assignBikes(workers, bikes))
workers = [[0,0],[1,1],[2,0]]; bikes = [[1,0],[2,2],[2,1]]
print(s.assignBikes(workers, bikes))
