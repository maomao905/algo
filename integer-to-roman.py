class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1: ('I','X','C','M'),
            5: ('V','L','D'),    
        }
        
        def get_roman(n, i):
            if 1 <= n <= 3:
                return roman[1][i] * n
            elif n == 4:
                return roman[1][i] + roman[5][i]
            elif 5 <= n <= 8:
                return roman[5][i] + roman[1][i] * (n-5)
            elif n == 9:
                return roman[1][i] + roman[1][i+1]
            else:
                return ''
        
        res = []
        i = 0
        while num > 0:
            num, n = divmod(num, 10)
            res.append(get_roman(n, i))
            i += 1
        
        res.reverse()
        return ''.join(res)
