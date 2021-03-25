from typing import List
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strings:
            diff = [0]
            for i in range(1,len(s)):
                d = ord(s[i]) - ord(s[i-1])
                if d < 0:
                    d += 26
                diff.append(d)
            
            seen[tuple(diff)].append(s)
        
        return list(seen.values())

s = Solution()
print(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
