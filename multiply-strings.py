class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0]
        carry = 0
        for i, n1 in enumerate(num1[::-1]):
            carry = 0
            for j, n2 in enumerate(num2[::-1]):
                k = i+j
                if len(res) < k+1:
                    res.append(0)
                m = int(n1) * int(n2) + carry + res[k]
                carry, q = divmod(m, 10)
                res[k] = q
            if carry:
                res.append(carry)
        ans = ''.join(map(str, res[::-1])).lstrip('0')
        return ans if ans else '0'

s = Solution()
print(s.multiply('2', '3'))
print(s.multiply('0', '0'))
print(s.multiply('123', '456'))
print(s.multiply('1234', '456'))
print(s.multiply('999', '9999'))
print(s.multiply('9133', '0'))
