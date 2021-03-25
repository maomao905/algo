"""
n=1 ()
n=2 (P) P() <--- ()() (()) ()() overlap
n=3 (P) (P) P() ()P ()P

time: n!
"""

from typing import List
# class Solution:
#     # def generateParenthesis(self, n: int) -> List[str]:
#     #     if n == 1:
#     #         return ['()']
#     # 
#     #     p = self.generateParenthesis(n-1)
#     # 
#     #     ht = set()
#     #     for _p in p:
#     #         ht.update(set(['()' + _p,  '(' + _p + ')', _p + '()']))
#     # 
#     #     return list(ht)
#     def generateParenthesis(self, n: int) -> List[str]:
#         result = []
#         def backtrack(comb, i):
#             # define the goal
#             if i == n:
#                 result.append(comb)
#                 return
# 
#             for j in (i, n+1):
# 
#         return list(ht)
"""
try all combinations
O(2^(2n) * N) N is for validation
    - binary choice ^ 2n
"""
# class Solution(object):
#     def generateParenthesis(self, n):
#         def generate(A = []):
#             if len(A) == 2*n:
#                 if valid(A):
#                     ans.append("".join(A))
#             else:
#                 print(A)
#                 import ipdb; ipdb.set_trace()
#                 A.append('(')
#                 generate(A)
#                 A.pop()
#                 A.append(')')
#                 generate(A)
#                 A.pop()
# 
#         def valid(A):
#             bal = 0
#             for c in A:
#                 if c == '(': bal += 1
#                 else: bal -= 1
#                 if bal < 0: return False
#             return bal == 0
# 
#         ans = []
#         generate()
#         return ans

"""
backtrack
try only valid combinations
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(S, left, right):
            """
            left: the number of opening brackets
            right: the number of closing brackets
            """
            # define the goal
            if len(S) == 2*n:
                result.append(S)
            
            # we can still have a room to add opening brackets
            if left < n:
                backtrack(S + '(', left + 1, right)
            
            # it is valid enough to add closing brackets
            if right < left:
                backtrack(S + ')', left, right + 1)
        
        backtrack('', 0, 0)
        return result

s = Solution()
print(s.generateParenthesis(3))
        
        
