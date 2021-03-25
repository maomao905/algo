"""
choices: 1~9
constraints: k numbers are used
             number is used at most once
goal: sum up to n

k=3, sum=9
1. [1, ?, ?]
    ? + ? = 8, without 1
2. [1, 2, ?]
    ? = 6

"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        
        def backtrack(remain_sum, comb, next_step):
            # define the goal
            if len(comb) == k and remain_sum == 0:
                results.append(list(comb))
                return
            
            # validate the constraints
            if len(comb) > k or remain_sum == 0:
                return
            
            for i in range(next_step, 9+1):
                comb.append(i)
                backtrack(remain_sum-i, comb, i+1)
                # backtrack the current choice
                comb.pop()
        
        backtrack(n, [], 1)
        return results

s = Solution()
print(s.combinationSum3(3, 7))
        
