"""
hash map of word and word index list

compare word1 index list and word2 index list and find the minimum difference

time O(N) space O(N)
"""
from typing import List
from collections import defaultdict
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        hm = defaultdict(list)
        for i in range(len(words)):
            hm[words[i]].append(i)
        
        w1_idx_list = hm[word1]
        w2_idx_list = hm[word2]
        
        i = j = 0
        min_diff = float('inf')
        
        while i < len(w1_idx_list) and j < len(w2_idx_list):
            min_diff = min(min_diff, abs(w1_idx_list[i] - w2_idx_list[j]))
            
            if w1_idx_list[i] < w2_idx_list[j]:
                i += 1
            else:
                j += 1
        
        return min_diff

s = Solution()
print(s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice'))
print(s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'makes'))
        
        
