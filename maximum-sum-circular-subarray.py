"""
1 intervals -> Kadane's algorithm
[i, j]
2 intervals
[0, i] + [j, end]
if [i, j] is min-subarray, [0,i] + [j, end] is maximum subaaray
max sum is total sum - min
"""
from typing import List
class Solution:
    def calculate_one_interval_max_subaaray(self, A):
        current_sum = 0
        max_sum = 0
        for n in A:
            current_sum = max(n+current_sum, 0)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    def calculate_min_subaaray(self, A):
        current_sum = 0
        min_sum = 0
        for n in A:
            current_sum = min(n+current_sum, 0)
            min_sum = min(min_sum, current_sum)
        return min_sum
    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_sum_one_interval = self.calculate_one_interval_max_subaaray(A)
        max_sum_two_interval = sum(A) - self.calculate_min_subaaray(A)
        
        m = max(max_sum_one_interval, max_sum_two_interval)
        if m == 0:
            return max(A)
        return m
"""
prefix sum + monotonic queue
"""
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        ans, prefix_sum = float('-inf'), 0
        monoq = deque([(-1, 0)]) # 0 at index -1
        
        for i, n in enumerate(A+A):
            if i - monoq[0][0] > len(A):
                monoq.popleft()
            prefix_sum += n
            ans = max(ans, prefix - monoq[0][1])
            while monoq and monoq[-1][1] >= prefix:
                monoq.pop()
            monoq.append((i, prefix))
            
        return ans

s = Solution()
print(s.maxSubarraySumCircular([1,-2,3,-2]))
print(s.maxSubarraySumCircular([5,-3,5]))
print(s.maxSubarraySumCircular([-2,-3,-1]))
