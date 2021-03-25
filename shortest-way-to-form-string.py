"""
hash map to store the source character and its positions
when there are multiple positions for the same character, binary search to find there
closest larger position

S: length of source, T: length of target
time O(S + TlogS) space O(S)
"""
from collections import defaultdict
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        pos = defaultdict(list)
        for i, s in enumerate(source):
            pos[s].append(i)
        
        cnt = 1
        prev_pos = -1
        
        for i, s in enumerate(target):
            if s not in pos:
                return -1
            
            # binary search
            s_pos = pos[s]
            l,r = 0, len(s_pos)
            while l<r:
                mid = l + (r-l)//2
                if prev_pos >= s_pos[mid]:
                    l = mid + 1
                else:
                    r = mid
            
            if l < len(s_pos):
                prev_pos = s_pos[l]
            else:
                cnt += 1
                prev_pos = s_pos[0]
            # print(s, prev_pos, cnt)
        return cnt

"""
create next index mapping O(26*S) = O(S)
  a b b c
  0 1 2 3
a 1 0 0 0
b 1 1 2 0
c 3 3 3 3
d 0 0 0 0
..
time O(S + T) space O(S)
"""
from collections import defaultdict
class Solution
    def shortestWay(self, source: str, target: str) -> int:
        pos = [[-1] * len(source) for _ in range(26)]
        for i, o in enumerate(range(ord('a'), ord('z')+1)):
            c = chr(o)
            prev = -1
            for j in reversed(range(len(source))):
                if source[j] == c:
                    pos[i][j] = j
                    prev = j
                else:
                    pos[i][j] = prev
        
        cnt = 1
        prev = 0 # keep track of the source string position
        for i, c in enumerate(target):
            j = ord(c)-ord('a')
            if pos[j][0] == -1:
                return -1
            
            cur = pos[j][prev] if prev < len(source) else -1
            # we have no matching character in source string, go back to first position where the current character appear in source string
            if cur == -1:
                cnt += 1
                prev = pos[j][0] + 1
            else:
                prev = cur + 1
        return cnt

s = Solution()
print(s.shortestWay('abc', 'abcbc'))
print(s.shortestWay('abc', 'acdbc'))
print(s.shortestWay('xyz', 'xzyxz'))
print(s.shortestWay("adbsc", "addddddddddddsbc"))
print(s.shortestWay("aaaaa", "aaaaaaaaaaaaa"))
