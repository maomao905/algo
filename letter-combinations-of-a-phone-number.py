"""
2 -> abc
3 -> def

ad ae af bd be bf cd ce cf

それぞれのdigitで使うcharacter indexをlistにappend
listの長さが、given digitsのlengthになったら結果を保存

N is the 3-letter digit length and M is the 4-letter digit length
time: O(3^N * 4^M)
space: O(N+M) for recursion stack
"""

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        digit_to_letter = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
        }
        
        res = []
        def recursive(comb):
            if len(comb) == len(digits):
                res.append(''.join(comb))
                return
            
            i = len(comb)
            
            for l in digit_to_letter[digits[i]]:
                comb.append(l)
                recursive(comb)
                comb.pop()
        
        recursive([])
        return res

s = Solution()
print(s.letterCombinations('23'))
print(s.letterCombinations(''))
print(s.letterCombinations('2'))
print(s.letterCombinations('349'))
            
            
        
