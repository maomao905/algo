"""
cumulative XOR

x ^ x = 0
<-----  cum sum  ---->
<-before-><--target-->
cum sum ^ before -> before numbers are xor twice, which becomes all zero
"""
from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N=len(arr)
        C = [0] * (N+1)
        
        for i in range(N):
            C[i+1] = C[i] ^ arr[i]
        
        return [C[l] ^ C[r+1] for l, r in queries]

s = Solution()
print(s.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))
print(s.xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]))
print(s.xorQueries(arr = [4,8,4,10], queries = [[2,3],[1,3],[0,0],[0,3]]))
