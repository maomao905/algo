"""
(WA)
even -> divide
odd  -> multiply
nums = [4,1,5,20,3]
odd  -> largest   5
even -> smallest  4

even can be odd
odd will be even
"""
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        odd_max = 0
        even_min = float('inf')
        for n in nums:
            if n % 2:
                odd_max = max(odd_max, n)
            else:
                even_min = min(even_min, n)
        
        def good(n):
            if odd_max < even_min:
                return odd_max <= n <= even_min
            else:
                return even_min <= n <= odd_max
        
        def update_odd_max(n):
            nonlocal odd_max
            if odd_max < even_min:
                odd_max = max(odd_max, n)
            else:
                odd_max = min(odd_max, n)
        
        def update_even_min(n):
            nonlocal even_min
            if odd_max < even_min:
                even_min = min(even_min, n)
            else:
                even_min = max(even_min, n)
            
            
        print('--', odd_max, even_min)
        get_diff = lambda x: min(abs(odd_max-n), abs(even_min-n))
        res = []
        for n in nums:
            cur = n
            if n % 2:
                diff = get_diff(n)
                old_diff = diff
                if get_diff(n*2) < diff:
                    n *= 2
                    diff = get_diff(n)
                update_odd_max(n)
                print(cur, '->', n, old_diff, '->', diff, 'odd_max:', odd_max, 'even_min:', even_min)
                res.append(n)
            else:
                diff = get_diff(n)
                while not good(n) and n % 2 == 0 and get_diff(n//2):
                    n //= 2
                    diff = get_diff(n)
                update_even_min(n)
                print(cur, '->', n, diff)
                res.append(n)
        print(res)
        return max(res) - min(res)

"""
even can be divided -> even can decrease
odd can be multiplied -> odd can increase

odd will be even after one operation
even can be odd after some operations

to simplify, first change odd to even by multipling odd
use heap to get maximum value to decrease
keep track of (max - min)

O(N*log(max value) * logN)

N*log(max value) is the maximum number of pop counts
"""
from heapq import *
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        N=len(nums)
        # convert odd to even
        for i in range(N):
            if nums[i] % 2:
                nums[i] *= -2
            else:
                nums[i] = -nums[i]
        
        min_num = -max(nums)
        heapify(nums)
        
        ans = float('inf')
        while nums:
            n = -heappop(nums)
            ans = min(ans, n - min_num)
            
            if n % 2:
                break
            
            # still even
            n //= 2
            min_num = min(min_num, n)
            heappush(nums, -n)
        
        return ans
                


s = Solution()
print(s.minimumDeviation([1,2,3,4]))
print(s.minimumDeviation([4,1,5,20,3]))
print(s.minimumDeviation([2,10,8]))
                
