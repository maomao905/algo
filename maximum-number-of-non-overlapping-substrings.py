"""
1. all contained
<----->
 <-->     <-- we should choose this
2. partially overlapped
<----->   <-- we should choose this
  <----->
3. non-overlapped
<----><--> both remain

stack

O(N) space O(N)
"""
from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        N=len(s)
        pos = {}
        for i in range(N):
            if s[i] not in pos:
                pos[s[i]] = [i, i]
            else:
                pos[s[i]][1] = i
        print(pos)
        stack = []
        for start, end in sorted(pos.values()):
            # non-overlapped
            if not stack or stack[-1][1] < start:
                stack.append((start, end))
            # all contained
            elif stack[-1][1] > end:
                stack.pop()
                stack.append((start, end))
        
        return [s[start:end+1] for start, end in stack]

"""
1. get first and last position of each character

       0 1 2 3 4 5 6 7 8 9 10
       a d e f a d d a c c c
       
       a c   d e f
first  0 8   1 2 3
last   7 10  6 2 3

2. get valid substrings and the range for each character (a-z)

consider 'a' range
1. abba
   ^  ^
2. baba -> invalid because we should choose b instead of b because the b starts before a
   ^ ^
3. abab -> expand the end to b's end
   ^  ^

3. merge intervals
sort intervals and append interval to result if previous character ends before current character starts

               aabcccab
interval of a  <------>
interval of b  b is invalid in step 2
interval of c     <->

O(N)
"""
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        def get_valid_interval(begin, end):
            interval = (begin, end)
            i = begin
            while i <= interval[1]:
                if pos[s[i]][0] < begin:
                    return
                if pos[s[i]][1] > interval[1]:
                    interval = (begin, pos[s[i]][1])
                i += 1
            return interval
                    
        N=len(s)
        pos = {}
        for i in range(N):
            if s[i] not in pos:
                pos[s[i]] = [i, i]
            else:
                pos[s[i]][1] = i
        
        intervals = []
        for c in pos:
            interval = get_valid_interval(pos[c][0], pos[c][1])
            if interval:
                intervals.append(interval)
        # merge intervals
        intervals.sort()
        res = []
        
        for begin, end in intervals:
            if res and end <= res[-1][1]:
                res.pop()
            res.append((begin, end))
        
        return [s[begin:end+1] for begin, end in res]

s = Solution()
print(s.maxNumOfSubstrings('adefaddaccc'))
print(s.maxNumOfSubstrings('abbaccd'))
print(s.maxNumOfSubstrings('aabcabc'))
print(s.maxNumOfSubstrings("cabcccbaa"))
print(s.maxNumOfSubstrings("bbcacbaba"))
