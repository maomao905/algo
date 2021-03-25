from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ans = []
        for i in reversed(range(len(digits))):
            s = digits[i] + carry
            carry = int(s == 10)
            ans.append(s%10)
        if carry:
            ans.append(1)
        return list(reversed(ans))
            
s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([9,9,9]))
print(s.plusOne([9,8,9]))
