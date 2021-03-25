"""
0<--s-->,i,<--s-->,j,<--s-->,k,<--s-->n

for j in range(N)
    store s in hashset if 0<--s-->,i,<--s-->,j
    find k such that j,<--s-->,k,<--s-->,n and s in hashset

O(N^2)
"""
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        N=len(nums)
        if N<7:
            return False
        C = list(accumulate(nums))

        # 0,i,i+1,j,j+1,k,n-1
        for j in range(3, N-3):
            
            s = set()
            for i in range(1,j-1):
                if C[i-1] == C[j-1] - C[i]:
                    s.add(C[i-1])
            
            for k in range(j+2,N-1):
                if C[k-1] - C[j] == C[N-1] - C[k] and C[k-1] - C[j] in s:
                    return True
        
        return False
            
s = Solution()    
print(s.splitArray([1,2,1,2,1,2,1]))
print(s.splitArray([1,2,3,3,1,-14,13,4]))
print(s.splitArray([-2, -24, -97, 32, 69, 41, 69, 52, 26, 32, 11, 12, 79, -64, 57, 50, 63, 98, 14, -21, -64, 52, 90, 71, 49, 7, 62, 46, 96, 94, 59, 29, 71, 81, 8, 48, -81, 68, 18, 99, 46, 97, 40, 42, -3, 65, 99, 44, 54, 30, 86, 42, 10, 95, 39, 96, 47, 45, 14, 12, 97, -24, 97, 81, 65, 25, 72, -30, 7, 58, 99, 53, -94, 1, -99, -62, 97, 29, 23, 45, 0, 2, -91, -13, 41, 44, 56, 8, 99, 70, 25, 22, 29, 22, 78, 50, -42, 87, 72, 64, 77, -83, 13, 85, 7, 43, -73, 90, 23, 69, 48, 76, 62]))
            
        
