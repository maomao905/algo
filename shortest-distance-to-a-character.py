from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        N=len(s)
        stack = []
        res = [0] * N
        last = float('-inf')
        for i in range(N):
            if s[i] == c:
                while stack:
                    j = stack.pop()
                    res[j] = min(i - j, j - last)
                last = i
            else:
                stack.append(i)
        
        while stack:
            j = stack.pop()
            res[j] = j - last
        
        return res

s = Solution()
print(s.shortestToChar('loveleetcode', 'e'))
                    
