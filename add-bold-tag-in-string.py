"""
for word in dict:
    find all matching position
    save start and end position

result is [[start, end], [start, end]]
sort and if end1 > start2, merge them

string matching takes (SL) each time in worst case
time: O(SLD) + O(D) + O(S) = O(SLD)
    S: string s size
    L: average dict string length
    D: dict size
"""
from typing import List
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        if not dict:
            return s
        def find_match_pos(word):
            pos = []
            start = 0
            while True: 
                r = s.find(word, start)
                if r == -1:
                    break
                pos.append([r, r + len(word)-1])
                start = r + 1
            return pos
        
        def merge(pos):
            merged = []
            
            for start, end in pos:
                if merged and merged[-1][1] >= start-1:
                    merged[-1][1] = max(merged[-1][1], end)
                else:
                    merged.append([start, end])
            return merged
        
        pos = []
        for word in dict:
            pos.extend(find_match_pos(word))
        
        # sort by start position
        pos.sort(key=lambda x: x[0])
        
        merged = merge(pos)
        if not merged:
            return s
        
        # print(merged)
        res = []
        cur = 0
        for start, end in merged:
            res.append(s[cur:start])
            res.append('<b>')
            res.append(s[start:end+1])
            res.append('</b>')
            cur = end + 1
        
        last_end = merged[-1][1]
        res.append(s[last_end+1:])
        return ''.join(res)

s = Solution()
# print(s.addBoldTag(s = "abcxyz123", dict = ["abc","123"]))
print(s.addBoldTag(s = "aaabbcc", dict = ["aaa","aab","bc"]))
            
