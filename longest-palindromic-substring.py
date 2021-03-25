"""
'abcdefgcbabcgfopqr'
-> fgcbabcgf
a only once, others(f~b) second times
-> a -> bab -> cbabc -> ...

'bbbbaabbbb'
"""
"""
Brute-force
O(N^3)
"""
class Solution:
    # abccba N//2 -> 3 even
    # abcba N//2 -> 2 odd
    # O(N)
    def is_palindrome(self, s):
        N = len(s)
        for i in range(N//2):
            end = N-1-i
            if s[i] != s[end]:
                return False
        return True
    
    # abcdefgcbabcgfopqr
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return ''
        max_len = 0
        ans = s[0]
        for i in range(len(s)):
            for j in range(i):
                subs = s[j:i+1]
                # print(subs)
                if self.is_palindrome(subs):
                    current_len = i+1-j
                    if max_len < current_len:
                        ans = subs
                        max_len = current_len
        
        return ans

"""
check only beginning and end of word
O(N^2)
space: O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        ans = s[0]
        for i in range(N):
            # consider i is center (odd length)
            for j in range(1,i+1):
                if not(0 <= i-j and i+j < N):
                    break
                if s[i-j] == s[i+j]:
                    if 2*j + 1 > len(ans):
                        ans = s[i-j:i+j+1]
                else:
                    break
            
            # even length
            # l r
            # 1 4 (2,3 are the center)
            k = i+1
            for j in range(i+1):
                if k >= N:
                    break
                if s[i-j] == s[k]:
                    if k+1-(i-j) > len(ans):
                        ans = s[i-j:k+1]
                else:
                    break
                
                k += 1
                
        return ans


"""
DP
ababa
if bab is palindrome, then if a == a, a/bab/a is palindrome
dp[i][j] = s[i] == s[j] and dp[i+1][j-1] (if i<j and j-i>=2)
'ab' s[0]=a s[1]=b dp[1][0] <--- wrong because j < i
'bab' s[0]=b s[2]=b  dp[1][1]

fill j-i <= 1 indivisually (2文字以内の場合)
j-i=0 'a'        always palindrome because it's a single character
j-i=1 'ab', 'bb' if s[i] == s[j], it's palindrome

row i: start
column j: end
dp[i][j] = True if s[i,j] is palindrome
how to find the longest palindrome? ->  max(j-i) where dp[i][j] == True
time: O(N^2) for DP table
space: O(N^2)
"""                    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        
        """
        i+1, j-1を毎回調べるので、iは後ろから、jは前から埋めていけば良い
            0 1 2 3 4
          0 ........ 
          1   6 7 8 9
          2     3 4 5
          3       1 2
          4
        """
        ans = s[0]
        for i in reversed(range(N)):
            for j in range(N):
                if j-i <= 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                
                if dp[i][j] and j-i+1 > len(ans):
                    ans = ans[i:j+1]
        
        return ans

"""
Manacher's algorithm
http://en.wikipedia.org/wiki/Longest_palindromic_substring
"""
class Solution:
    
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
                
        
s = Solution()
print(s.longestPalindrome('acaac'))
# print(s.longestPalindrome('aaaabbaa'))
# print(s.longestPalindrome('babad'))
# print(s.longestPalindrome('cbbd'))
# print(s.longestPalindrome('a'))
# print(s.longestPalindrome('ac'))
# print(s.longestPalindrome(''))
# print(s.longestPalindrome('a'))
