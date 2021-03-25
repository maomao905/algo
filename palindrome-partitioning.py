"""
how to partition
-> backtracking
generate all possible combinations and check if it is a palindrome

すべての文字それぞれで、current bucketに入れるか、入れないかの２通りあるので O(2^N)
毎回、string生成や結果のリストcopy、palindrome checkがあるのでO(N)
time: O(N*2^N)
space: O(N) for recursion stack
"""
from typing import List
class Solution:
    # O(N)
    def is_palindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        def dfs(comb, start):
            # goal
            if start > len(s)-1:
                # O(N)
                res.append(list(comb))
            
            # choose
            """
            every start, check all [start, start...end]
            if it's palindrome, continue dfs = move start to end + 1
            """
            for i in range(start, len(s)):
                subs = s[start:i+1]
                comb.append(subs)
                # constraint
                if self.is_palindrome(subs):
                    dfs(comb, i+1)
                # backtrack
                comb.pop()
                
        res = []
        dfs([], 0)
        return res

"""
dynamic programming
abcba
c is palindrome ith
bcb is palindrome s[i-1] == s[i+1]
abcba is palindrome s[i-2] == s[i+2]

backtrackingを使わなくても、現在の結果を保存して、追加していけばいける
O(N*2^N)だが、palindrome checkがなくなる
space: O(N^2)
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def dfs(comb, start):
            if start >= N:
                res.append(list(comb))
            
            for end in range(start, N):
                if end - start < 2:
                    memo[start][end] = s[start] == s[end]
                else:
                    memo[start][end] = s[start] == s[end] and memo[start+1][end-1]
                
                if memo[start][end]:
                    comb.append(s[start:end+1])
                    dfs(comb, end+1)
                    comb.pop()
        
        N = len(s)
        memo = [[False] * N for _ in range(N)]
        res = []
        dfs([], 0)
        return res

s = Solution()
# print(s.partition('aab'))
# print(s.partition('abcba'))
print(s.partition('aaaaa'))
