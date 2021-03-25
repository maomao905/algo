from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = Counter(s)
        
        odd_num = 0
        for n in cnt.values():
            if n % 2 == 1:
                odd_num += 1
        
        return odd_num == len(s) % 2

s = Solution()
print(s.canPermutePalindrome('aab'))
print(s.canPermutePalindrome('carerac'))
print(s.canPermutePalindrome('codeco'))
