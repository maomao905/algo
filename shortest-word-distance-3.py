from typing import List

class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        w1 = w2 = None
        
        ans = float('inf')
        for i, w in enumerate(words):
            if w == word1 and w == word2:
                if w1 is None:
                    w1 = i
                elif w2 is None:
                    w2 = i
                elif w1 < w2:
                    w1 = i
                else:
                    w2 = i
            elif w == word1:
                w1 = i
            elif w == word2:
                w2 = i
            
            if w1 is not None and w2 is not None:
                ans = min(ans, abs(w1-w2))
        
        return ans

class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        w1, w2 = float('-inf'), float('inf')
        
        ans = float('inf')
        same = word1 == word2
        for i, w in enumerate(words):
            if w == word1:
                w1 = i
            if w == word2:
                if same:
                    # always w1 < w2
                    w1 = w2
                w2 = i
            
            ans = min(ans, abs(w2-w1))
        
        return ans
                
s = Solution()
print(s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding'))
print(s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'makes'))
print(s.shortestWordDistance(["makes", "coding", "makess", "coding", "makes"], 'makes', 'makes'))
print(s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"],"coding","practice"))
