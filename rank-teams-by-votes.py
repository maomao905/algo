"""
sort 'ABC' by the matrix below
  1  2  3
A -5 0  0 A
B 0 -2 -3 B
C 0 -3 -2 C

    1  2  3
A  -2 -2 -2 A
B  -2 -2 -2 B
C  -2 -2 -2 C

M: number of vote character
N: length of votes
time O(NM + M^2logM)
space O(M^2)
"""

from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        cnt = {v: ([0] * len(votes[0])) + [v] for v in votes[0]}
        
        # O(NM)
        for v in votes:
            for i, _v in enumerate(v):
                cnt[_v][i] -= 1
        
        # O(M^2logM)
        return ''.join(sorted(votes[0], key=cnt.get))

s = Solution()
print(s.rankTeams(votes = ["ABC","ACB","ABC","ACB","ACB"]))
print(s.rankTeams(votes = ["WXYZ", "XYZW"]))
print(s.rankTeams(votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
        
