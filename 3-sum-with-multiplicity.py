from collections import Counter
from typing import List
"""
(WA)
cnt = Counter(arr)
fix two elements and last one is automatically decided
fix one element -> then fix one element -> check if remain exists by hashmap

O(D^2) D: num of distinct values
O(n^2) in worst when all values of arr are different
"""
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        cnt = Counter(arr)
        choices = sorted(list(cnt.keys()))
        N=len(choices)
        
        def get_count(i,j,k):
            n = len(set([i,j,k]))

            if n == 1:
                return 6
            elif n == 2:
                return 2
            else:
                return 1
        
        def check(cnt, i):
            res = 0
            for j in range(i, N):
                n = choices[j]
                if cnt[n]:
                    remain = target - choices[i] - n
                    if remain < n:
                        break

                    # if cnt[remain]:
                    #     print(choices[i], n, remain, cnt[remain])
                    mul = cnt[n]
                    cnt[n] -= 1
                    if cnt[remain]:
                        res += cnt[remain] * mul // (get_count(choices[i], n, remain) or 1)
                    cnt[n] += 1

            return res
        
        ans = 0
        for i in range(N):
            n = choices[i]
            mul = cnt[n]
            cnt[n] -= 1
            ans += int(check(cnt, i) * mul)
            cnt[n] += 1
        return ans % (10**9+7)

"""
N: len of arr
D: num of distinct values of arr
O(N + D^2) N for counting arr
O(N^2) worst case when all values of arr are different
"""
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        cnt = Counter(arr)
        ans = 0
        for i in cnt:
            for j in cnt:
                k = target - i - j
                if i == j == k:
                    ans += cnt[i] * (cnt[i]-1) * (cnt[i]-2) // 6
                elif i == j:
                    ans += cnt[i] * (cnt[i]-1) //2 * cnt[k]
                elif i < j < k: # make sure i,j,k pair counted once
                    ans += cnt[i] * cnt[j] * cnt[k]
        return ans % (10**9+7)
        
            
s = Solution()
print(s.threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))
print(s.threeSumMulti([1,1,2,2,2,2], 5))
print(s.threeSumMulti([0,0,0], 0))
print(s.threeSumMulti([3,3,1], 7))
print(s.threeSumMulti([0,0,1,2,3], 3))

                
