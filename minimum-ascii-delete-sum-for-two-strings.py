"""
memorization
O(MN) space O(MN)
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        M,N=len(s1),len(s2)
        memo = {}
        def helper(i,j):
            if i == M and j == N:
                return 0
            if (i,j) not in memo:
                if i == M:
                    memo[i,j] = sum(ord(char) for char in s2[j:])
                elif j == N:
                    memo[i,j] = sum(ord(char) for char in s1[i:])
                elif s1[i] == s2[j]:
                    memo[i,j] = helper(i+1, j+1)
                else:
                    memo[i,j] = min(helper(i+1, j) + ord(s1[i]), helper(i, j+1) + ord(s2[j]))
            return memo[i,j]
        
        return helper(0,0)

s = Solution()
print(s.minimumDeleteSum('sea', 'eat'))
print(s.minimumDeleteSum('sea', 'sea'))
print(s.minimumDeleteSum('delete', 'leet'))
        
            
            
