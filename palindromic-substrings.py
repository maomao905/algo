"""
brute-force
check all substrings O(N^3)
    - substrings patterns O(N^2)
    - make substring O(N) and check palindrome O(N)

check each substring and as long as it's palindrome, expand the range (left and right)
    - good thing is we don't need to check entire substring and only the new characters (left and right) O(1)

O(N^2), space O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            
            # odd length
            j = k = i
            while 0 <= j and k < len(s):
                if s[j] == s[k]:
                    cnt += 1
                    j -= 1
                    k += 1
                else:
                    break
            
            # even length    
            j = i
            k = i+1
            while 0 <= j and k < len(s):
                if s[j] == s[k]:
                    cnt += 1
                    j -= 1
                    k += 1
                else:
                    break
        
        return cnt

s = Solution()
print(s.countSubstrings('abc'))
print(s.countSubstrings('aaaaa'))
