from decimal import Decimal

class Solution:
    def myPow(self, x: Decimal, n: int) -> Decimal:
        ans = 1
        
        N = abs(n)
        try:
            while abs(N) > 0:
                if N % 2 == 1:
                    ans = ans * x
                N //= 2
                x **= 2
                # print(n,x,ans)
        except:
            print(N,x,ans)
        return ans if n > 0 else 1/ans

s = Solution()
print(s.myPow(2.00000, 6))
# print(s.myPow(3.00000, 3))
print(s.myPow(2.00000, -2))
print(s.myPow(2.00000, -2147483648))

"""

2 ** 6
x = 2, n = 6

ans x n
1   2 6
2   4 3
2   16 1

16 1

2 ** 6 -> 2 ** 3 ** 2
2 ** 3 -> 2 ** 2 * 2

2 ** 6 -> 2 ** 1 * 2

3   3**1
9   3**2
27  3**3 -> 3//2 -> 1 (3**1) ** 3
81  3**4 -> (3**2)**2
    3**8 -> ((3**2)**2)**2
    3**9 -> ((3**2)**2)**2 * 3

3 ** -1 -> 1/3
3 ** -2 -> (3**-1) ** 2
4 -> 2 -> 1 O(logn)


3**4 -> 3 ** 2 ** 2
3**3 -> 3 ** 2 * 3
"""
