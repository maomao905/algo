"""
heap

use most frequent char first
but if it's not k distance apart, pop and push back

O(N*26log26) = O(N)
it's not efficient
"""
from collections import deque, Counter
from heapq import *
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        N=len(s)
        res = []
        heap = [(-cnt, c, -k) for c, cnt in Counter(s).items()]
        heapify(heap)
        
        for i in range(N):
            tmp = []
            while heap and heap[0][2] > i-k:
                tmp.append(heappop(heap))
            
            if not heap:
                return ''
            
            cnt, c, j = heappop(heap)
            res.append(c)
            if -cnt > 1:
                heappush(heap, (cnt+1, c, i))
            
            for item in tmp:
                heappush(heap, item)
        
        return ''.join(res)

"""
heap (more efficient)

once the char is used, freeze(keep) the char k times separately
after k times, push back into heap

it ensures only logN per character

O(Nlog26) = O(N)
"""
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        N=len(s)
        res = []
        heap = [(-cnt, c) for c, cnt in Counter(s).items()]
        heapify(heap)
        freeze = deque()
        
        while heap:
            cnt, c = heappop(heap)
            res.append(c)
            freeze.append((cnt+1, c))
            if freeze and len(freeze) >= k:
                cnt, c = freeze.popleft()
                if cnt < 0:
                    heappush(heap, (cnt, c))
        return ''.join(res) if len(res) == N else ''

"""
bucket

allocate most frequent char with k distance each other
then allocate next frequent char with k distance each other
continue this process
"""
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not k:
            return s
        
        N=len(s)
        cnt = Counter(s)
        sorted_cnt = cnt.most_common()
        most_freq = sorted_cnt[0][1]
        if (most_freq-1) * k + list(cnt.values()).count(most_freq) > N:
            return ''
        
        res = [''] * N
        i = (N-1) % k
        for c, freq in sorted_cnt:
            for _ in range(freq):
                res[i] = c
                i += k
                if i >= N:
                    i = (i-1) % k
        
        return ''.join(res)

s = Solution()
print(s.rearrangeString('aabbcc', 3))
print(s.rearrangeString('aaabc', 3))
print(s.rearrangeString('aaadbbcc', 2))
print(s.rearrangeString('aaaaaaa', 2))
print(s.rearrangeString('aa', 0))
print(s.rearrangeString('aabbcc', 4))
