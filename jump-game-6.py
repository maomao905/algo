"""
(TLE)
dp[i] = maximum score at ith index
time O(NK)
"""

from typing import List

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N=len(nums)
        dp = [float('-inf')] * N
        
        dp[0] = nums[0]
        for i in range(N-1):
            for j in range(i+1,min(i+k+1,N)):
                dp[j] = max(dp[i] + nums[j], dp[j])
        
        return dp[-1]

"""
(WA)
take the step which has the maximum score

[10,-5,-2,4,0,3], k = 3

if the value is positive, we must take the step (because there is a chance to increase the sum)
if the value is non-positive, we want to avoid but 

choosing max(negatives) does not necessarily lead to best sum like the example below
[0 -1 -2 -4 1] k=2, assuming we are at 0
   -1    -4 1  sum is -4
      -2    1  sum is -1
=> maximize the sum of negative arrays given k steps
for j in range(i,i+k)
    dp[j] = max(dp[i] + nums[j], dp[i])

cumulative sum
"""
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N=len(nums)
        dp = [float('-inf')] * N
        
        dp[0] = nums[0]
        
        for i in range(N-1):
            for j in range(i+1, min(i+k+1, N)):
                dp[j] = max(dp[i] + nums[j], dp[j])
                if nums[j] > 0:
                    break
            
        return dp[-1]

"""
DP + deque

dp[i] = max score ending at ith index
<---k--->i you can jump from anywhere within k steps to i th index
it means you only have to care about last k steps and maximize the score of i position
push/pop queue only once per position -> O(N)

use monotonically decreasing queue
    queue maintains index but queue's order is dp's score
    queue[0] is always the highest score and q[-1] is minimum score(current score)
    dp[i] = dp[queue[0]] + nums[i]
    it ensures dp[i] comes from highest score

time O(N) space O(N)
"""
from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N=len(nums)
        q = deque([0])
        dp = [0] * N
        dp[0] = nums[0]
        for i in range(1,N):
            # remove out of range (old) element
            while q and q[0] < i - k:
                q.popleft()
            
            # now q[0] is the highest score, jump from q[0]
            dp[i] = dp[q[0]] + nums[i]
            
            # keep monotonically decreasing order in queue
            while q and dp[q[-1]] < dp[i]:
                q.pop()
            q.append(i)
        return dp[-1]

"""
heap
get the maximum score in the window -> heap

time O(NlogN) space O(N)
"""
from heapq import *
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N=len(nums)
        heap = [] # (score, index)
        score = 0
        for i in range(N):
            while heap and heap[0][1] < i - k:
                heappop(heap)
            
            if heap:
                score = -heap[0][0] + nums[i]
            else:
                score = nums[i]
            
            heappush(heap, (-score, i))
        return score

"""
(TLE)
segment tree
get the maximum score within the range logN time and add to current value
then update the current score logN
time O(NlogN) space O(N)
"""
class Node():
    def __init__(self, start, end):
        self.start = start # start index in the array
        self.end = end # end index in the array
        self.left = None # left subtree
        self.right = None # right subtree
        self.val = 0

class SegTree():
    # O(2N) = O(N)
    def __init__(self, arr):
        def build(arr, l, r):
            node = Node(l, r)
            if l == r:
                node.val = arr[l]
                return node
            
            mid = (l + r) // 2
            node.left = build(arr, l, mid)
            node.right = build(arr, mid+1, r)
            
            node.val = self.merge(node.left.val, node.right.val)
            return node
        
        self.root = build(arr, 0, len(arr)-1)
    
    # O(logN)
    def update(self, i, val):
        def _update(node, i, val):
            if node.start == node.end:
                node.val = val
                return val
            
            mid = node.start + (node.end - node.start)//2
            if i <= mid:
                _update(node.left, i, val)
            else:
                _update(node.right, i, val)
            
            node.val = self.merge(node.left.val, node.right.val)
            return node.val
        
        return _update(self.root, i, val)
            
    
    # O(logN)
    def query(self, i, j):
        """
        sum of arr[i..j]
        """
        def _query(node, i, j):
            if node.start == i and node.end == j:
                return node.val
            
            mid = node.start + (node.end - node.start)//2
            
            # left subtree
            if j <= mid:
                return _query(node.left, i, j)
            # right subtree
            elif i > mid:
                return _query(node.right, i, j)
            else:
                return self.merge(_query(node.left, i, mid), _query(node.right, mid+1, j))
        
        if i > j:
            return 0
        return _query(self.root, i, j)
    
    def merge(self, x, y):
        return max(x, y)

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        N=len(nums)
        tree = SegTree([nums[0]] + nums[1:])
        
        ans = 0
        for i in range(1,N):
            # get the maximum score within k range
            max_score = tree.query(max(i-k, 0), i-1)
            
            max_score += nums[i]
            if i == N-1:
                ans = max_score
            
            # update the current max score
            tree.update(i, max_score)
        
        return ans
        

s = Solution()
print(s.maxResult(nums = [1,-1,-2,4,-7,3], k = 2))
print(s.maxResult(nums = [10,-5,-2,4,0,3], k = 3))
print(s.maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2))
print(s.maxResult(nums = [100,-1,-100,-1,100], k = 2))
print(s.maxResult(nums = [10,5,2], k = 2))
