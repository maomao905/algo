class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pair = {
            '6': '9',
            '9': '6',
            '8': '8',
            '1': '1',
            '0': '0'
        }

        N=len(num)
        l, r = 0, N-1
        while l<r:
            if num[l] not in pair or pair[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        
        return num[l] in ('0','1','8') if l == r else True
