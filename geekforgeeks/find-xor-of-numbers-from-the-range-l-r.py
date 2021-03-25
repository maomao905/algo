"""
           xor so far
0  0000 -> 0000
1  0001 -> 0001
2  0010 -> 0011
3  0011 -> 0000
---------------
4  0100 -> 0100 --> we have exactly same as original number because previous xor is 0
5  0101 -> 0001 --> second is always 1 because difference with previous num is only rightmost 1
6  0110 -> 0111 --> third is always n+1 because previous is 0001
7  0111 -> 0000 --> zero
---------------
8  1000 -> 1000 --> we have exactly same as original number
9  1001 -> 0001
10 1010 -> 1011
11 1011 -> 0000
---------------
12 1100 -> 1100 --> we have exactly same as original number

the reason why we get 0 every 4 steps is xor 1 twice in 4 step, which is zero

O(N)
"""
def get_answer(l, r):
    ans = 0
    for i in range(l, r+1):
        ans ^= i
    return ans

def get_cumulative_xor(n):
    mod = n % 4
    if mod == 0:
        return n
    elif mod == 1:
        return 1
    elif mod == 2:
        return n+1
    else:
        return 0

"""
xor twice to offset left cumulative xor
"""
def rangeXOR(l, r):
    return get_cumulative_xor(l-1) ^ get_cumulative_xor(r)

def xor(n, m):
    def xor(n):
        i = 1
        ans = 1 if 2 <= (n + 1) % 4 <=3 else 0
        while 1<<i <= n:
            x = (n + 1) % (1<<(i+1)) - (1<<i)
            if x > 0:
                ans += (x%2) * 1<<i
            i += 1
        return ans
    return xor(n-1)^xor(m)

from random import *
for _ in range(100):
    a, b = randint(0, 30), randint(0, 30)
    x, y = min(a,b), max(a,b)
    if rangeXOR(x, y) != get_answer(x, y):
        print(x, y, rangeXOR(x, y), get_answer(x, y))
        break
