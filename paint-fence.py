"""
scenario
1. use a different color from the previous post
2. use the same color as the previous post

if i-2 and i-1 use the same color -> i must use a different color
    i-2 i-1 i
    k   k   (k-1)
else if i-2 and i-1 use the different color -> i can use any color
    i-2 i-1 i
    k   k-1 k

num(i) = num_same_color(i) + num_diff_color(i)

num_same_color(i) = num_diff_color(i-1)
num_diff_color(i) = 
    num_same_color(i-1) * k-1 (i cannot choose the same color again)
    +
    num_diff_color(i-1) * k-1 (i needs to choose different color from the i-1)

use loop instead of recursion to avoid maximum recursion depth error
"""

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return k
        
        same, diff = k, k*(k-1)
        
        for i in range(3, n+1):
            same, diff = diff, (same + diff) * (k - 1)
        return same + diff

s = Solution()
print(s.numWays(3,2))
