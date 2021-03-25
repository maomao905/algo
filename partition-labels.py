"""
ababcbacadefegdehijhklij
a       ^
 b      ^
    c   ^
         d    ^
          e    ^
           f   ^
             g ^
                h  ^ 
                 i    ^
                  j    ^
"ababcbaca", "defegde", "hijhklij"
O(26*N) = O(N)
O(26) = O(1)
"""
from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        cur_letters = set()
        start = temp_start = end = 0
        target = S[0]
        partition = []
        while end < len(S):
            for i in range(temp_start, len(S)):
                if S[i] == target:
                    end = i
            
            for i in range(temp_start, end):
                if S[i] != target:
                    cur_letters.add(S[i])
            
            print(target, cur_letters, [start, temp_start, end])
            if len(cur_letters) > 0:
                target = cur_letters.pop()
                temp_start = end + 1
            else:
                partition.append(end-start+1)
                start = temp_start = end = end + 1
                if start < len(S):
                    target = S[start]
                cur_letters = set()
        return partition

"""
simpler solution with same approach
1. save last index for each letter
2. keep the rightmost boundary while iterating and if the current index is rightmost, then add it to result
rightmost boundary = largest last index up to current index
time: O(N)
space: O(N)
"""
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        left = right = 0
        
        last = {s: i for i, s in enumerate(S)}
        partition = []
        for i, s in enumerate(S):
            right = max(right, last[s])
            if right == i:
                partition.append(i - left + 1)
                left = i + 1
        return partition

s = Solution()
print(s.partitionLabels('ababcbacadefegdehijhklij'))
