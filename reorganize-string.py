"""
S = 'aab'
aba

brute-force O(2^N)
generate all combinations 2^N and exclude if next letter is the same N

backtracking N + O(2^N) -> TLE (we don't have to generate all patterns, so it's not efficient)
counter hash map
{a: 2, b: 1}
a {a: 1, b: 1}
b {a: 0, b: 1}
"""

from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        def recursive(comb):
            nonlocal ans
            if len(comb) == len(S):
                ans = ''.join(comb)
                return True
            
            prev = comb[-1] if len(comb) > 0 else ''
            for s in counter:
                if s == prev:
                    continue
                
                if counter[s] == 0:
                    continue
                
                comb.append(s)
                counter[s] -= 1
                if recursive(comb):
                    return True
                comb.pop()
                counter[s] += 1
            
            return False
            
        counter = Counter(S)
        ans = ''
        recursive([])
        return ans

"""
first create unique character, which appear only once
['', 'x', '', y, '']
insert the characters which appear more than once
"""

# class Solution:
#     def reorganizeString(self, S: str) -> str:
#         counter = Counter(S)
# 
#         letters = [''] * len(S)
# 
#         for l, freq in counter.items():
#             if freq == 1:
# 

"""
heap

aabbbc -> bababc
max-heap [b:3, a:2, c:1]
pop b, b:2
pop a, a:1 push back b:2 into heap
pop b, b:1 a's count is 0, no need to push back
pop c, c:0 push back b:1 into heap
pop b, b:0 c's count is 0, no need to push back
heap is empty and b's count is 0, it is good

time: O(NlogA) A: size of alphabet, N: because we have to pop all strings from heap
space: O(A) = O(1)
"""

import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = Counter(S)
        counter = sorted(counter.items(), key=lambda x: x[1])
        heap = [(-freq, letter) for letter, freq in counter]
        heapq.heapify(heap)
        
        ans = []
        prev = None
        while len(heap) > 0:
            freq, letter = heapq.heappop(heap)
            ans.append(letter)
            if prev is not None and prev[0] != 0:
                heapq.heappush(heap, prev)
            
            prev = (freq+1, letter)
            
        if prev and prev[0] != 0:
            return ''
        else:
            return ''.join(ans)

        
s = Solution()
print(s.reorganizeString('aabbbc'))
print(s.reorganizeString('aaab'))
        
