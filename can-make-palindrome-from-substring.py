"""
l..r 
rearrange
replace up to k of them with any letter

1. check if it's palindrome
    - count
    - other letters are even count
    - only one letter at most can be odd count

2. make palindrome by replacement
    - too many odd -> even
    - 3 odds 1 even -> 1 odd 3 even
        abcdd -> bbcdd
        replace odd with odd
    - 2 odd 1 even -> 2 even
        abcc -> aacc
        replace odd with odd
    - 4 odd 1 even -> even
        abcd
    - j odd
        - if j is even, j/2 odd replaced with other j/2
            - if j/2 > k, impossible to make palindrome
        - if j is odd, (j-1)/2 odd replaced with other (j-1)/2, 1 odd stays
            - aaabbbccc -> aabbbbbcc
            - if (j-1)/2 > k, impossible to make palindrome

time: O(N) + O(Q) Q: number of queries
O(N) for making cumulative counter
O(1) for each query O(26) = O(1)
"""
from typing import List
from collections import Counter
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        N=len(s)
        cnt = [None] * N
        cur_cnt = Counter()
        # cumulative counter
        for i in range(N):
            cur_cnt[s[i]] += 1
            cnt[i] = Counter(cur_cnt)
        
        res = []
        for l, r, k in queries:
            cur_cnt = cnt[r] if l == 0 else cnt[r] - cnt[l-1]
            # print(cur_cnt)
            odd_cnt = len([c for c in cur_cnt.values() if c%2])
            res.append(odd_cnt//2 <= k)
        return res

s = Solution()
print(s.canMakePaliQueries(s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
            
            
