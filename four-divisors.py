"""
1. get divisors O(sqrt of number)

O(sqrt(max number)*N)
"""
from typing import List
import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            div = set([1,n])
            for i in range(2,int(math.sqrt(n))+1):
                j, r = divmod(n, i)
                if r == 0:
                    div.update([i,j])
                if len(div) > 4:
                    break
            
            if len(div) == 4:
                ans += sum(div)
        return ans

s = Solution()
print(s.sumFourDivisors([21,4,7]))
print(s.sumFourDivisors([1,2,3,4,5,6,7,8,9,10]))
print(s.sumFourDivisors([7286,18704,70773,8224,91675]))
