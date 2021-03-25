class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        ptr = 0
        for d, n in shift:
            if d == 1:
                ptr -= n
            else:
                ptr += n
        ptr %= len(s)
        return s[ptr:] + s[:ptr]
        
