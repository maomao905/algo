"""
DP

parentheses is boundary
where can boundary exist?
    - '-+*'
    - we can calculate before the '-+*' and after the '-+*'

recursion
    - we can split and then split until it only contains digit
    - use memorization
"""

from typing import List

class Solution:
    def diffWaysToCompute(self, input: str, memo={}) -> List[int]:
        def calc(r1,r2,op):
            if op == '+':
                return r1+r2
            elif op == '-':
                return r1-r2
            else:
                return r1*r2
        
        if input.isdigit():
            return [int(input)]
        
        if input in memo:
            return memo[input]
        
        res = []
        for i in range(len(input)):
            if input[i] in '-+*':
                for r1 in self.diffWaysToCompute(input[:i]):
                    for r2 in self.diffWaysToCompute(input[i+1:]):
                        r = calc(r1,r2,input[i])
                        res.append(r)
        memo[input] = res
        
        return res

s = Solution()
print(s.diffWaysToCompute('2-1-1'))
print(s.diffWaysToCompute('2*3-4*5'))
