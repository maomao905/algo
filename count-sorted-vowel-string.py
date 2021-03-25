"""
recursion without memorization
time: O(5^N)
"""

class Solution:
    def countVowelStrings(self, n: int) -> int:
        def recursive(i, comb=[]):
            if len(comb) == n:
                nonlocal cnt
                cnt += 1
                return
            
            for j in range(i, 5):
                comb.append(choices[j])
                recursive(j)
                comb.pop()
        
        choices = ['a', 'e', 'i', 'o', 'u']
        cnt = 0
        recursive(0)
        return cnt

"""
recursion with memorization
time: O(5 * N) = O(N) space: O(N) N recursion stack
"""
class Solution:
    def countVowelStrings(self, n: int) -> int:
        def recursive(i, remain):
            if remain == 0:
                return 1

            if (i, remain) in memo:
                return memo[(i, remain)]

            cnt = 0
            for j in range(i, 5):
                cnt += recursive(j, remain-1)

            memo[(i, remain)] = cnt
            return cnt

        memo = {}
        return recursive(0, n)

s = Solution()
print(s.countVowelStrings(1))
print(s.countVowelStrings(2))
print(s.countVowelStrings(5))
