"""
time O(NlogK) space O(K)
"""

from typing import List

from heapq import *
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        return nsmallest(k, cnt, key=lambda w: (-cnt[w], w))

s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))
