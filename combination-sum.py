"""
backtracking
time: O(N^T) N: size of candidates T: target value
space: O(target/min_candidate)
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        def backtrack(remain_sum, comb, next_step):
            # define the goal
            if remain_sum == 0:
                results.append(list(comb))
                return
            
            # validate the constraints
            if remain_sum < 0:
                return
            
            for i in range(next_step, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain_sum-candidates[i], comb, i)
                # backtrack the current choice
                comb.pop()
        
        backtrack(target, [], 0)
        return results

s = Solution()
# print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([6,2,7,3], 7))
        
        
        
        
