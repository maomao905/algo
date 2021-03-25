"""
taking the all difference up to ith index
add +1 to the counter of the difference

[9,4,7,2,10]
counter{diffrence: count}
9 {}
4 {-5:1}
7 {-2:1,3:1}
2 {-7:1,-2:1,-5:1}
10 {1:1,6:1,3:2,8:1}

[20,1,15,3,10,5,8]
20 {}
1  {-19:1}
15 {14:1}
3  {-17:1,-12:1}
10 {-10:1,9:1,7:1}
5  {-15:1,4:1,-10:1,2:2,-5:3}

we should not delete the hash map of previous entry because there might be a same number before the current num,
it causes invalid count
3 13 13 23 23 33 33
3 {}
13 delete
13 delete
23 {10: 2}
23 {0: 1}
33 {10: 1} <-- it should be 3

time O(N^2) space O(N^2)
"""

from typing import List

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N=len(A)
        cnt = [{} for _ in range(N)]
        max_len = 0
        for i in range(N):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in cnt[j]:
                    cnt[i][diff] = cnt[j][diff] + 1
                else:
                    cnt[i][diff] = 2
                max_len = max(max_len, cnt[i][diff])
        return max_len

s = Solution()
# print(s.longestArithSeqLength([3,6,9,12]))
# print(s.longestArithSeqLength([9,4,7,2,10]))
# print(s.longestArithSeqLength([20,1,15,3,10,5,8]))
print(s.longestArithSeqLength([44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]))
                    
        
