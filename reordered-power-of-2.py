class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        cnt = Counter(str(n))
        
        return any(cnt == Counter(str(1<<i)) for i in range(31))
