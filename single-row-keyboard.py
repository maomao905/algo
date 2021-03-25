class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = {c: i for i, c in enumerate(keyboard)}
        
        ans = 0
        prev = 0
        for c in word:
            ans += abs(pos[c] - prev)
            prev = pos[c]
        return ans
