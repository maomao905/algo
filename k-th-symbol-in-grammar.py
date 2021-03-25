"""
brute-force time and space O(2^n)

only consider Kth element
time and spaceO(N)
row 4, K 5  01101001
row 3, K 3  0 1 1 0
row 2, K 1  0   1
row 1, K 0  0
"""

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 0:
            return 0
        
        parent = self.kthGrammar(N-1, (K+1)//2)
        # XOR
        return 1 - (K % 2) ^ parent
        # if parent == 1:
        #     if K % 2 == 1:
        #         return 1
        #     else:
        #         return 0
        # else:
        #     if K % 2 == 1:
        #         return 0
        #     else:
        #         return 1

s = Solution()
print(s.kthGrammar(1,1))
print(s.kthGrammar(2,1))
print(s.kthGrammar(2,2))
print(s.kthGrammar(4,5))
            
    
