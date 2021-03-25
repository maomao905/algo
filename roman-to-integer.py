class Solution:
    def romanToInt(self, s: str) -> int:
        order = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        sub = {
            'V': 4,
            'X': 9,
            'L': 40,
            'C': 90,
            'D': 400,
            'M': 900,
        }
        
        ans = 0
        stack = []
        for c in s:
            if stack and order[stack[-1]] < order[c]:
                stack.pop()
                ans += sub[c]
            else:
                stack.append(c)
        
        return ans + sum(order[c] for c in stack)

s = Solution()
print(s.romanToInt('III'))
print(s.romanToInt('IV'))
print(s.romanToInt('IX'))
print(s.romanToInt('LVIII'))
print(s.romanToInt('MCMXCIV'))
        
