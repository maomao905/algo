"""
brute-force
    - divide by 2,3,5 form 2 to until n is satified
    - 2,3,5 multiply by from 1 up to n

greatest common factor of 2,3,5 is 30
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30

n=10 -> 12
n=100 22/100 * 30 + gcf[12]


three pointers
uply number must be multiplied by ugly number
make sure we pick everything and avoid duplicates by choosing minimum every time and update one pointer

p2  p3  p5
1   1   1   min(2,3,5) = 2 increment p2 ugly = [1, 2]
2   1   1   min(4,3,5) = 3 increment p3 ugly = [1,2,3]
2   2   1   min(4,6,5) = 4 increment p2 ugly = [1,2,3,4]
3   2   1   min(6,6,5) = 5 increment p5 ugly = [1,2,3,4,5]
3   2   2   min(6,6,10) = 6 increment p2 and p3 ugly = [1,2,3,4,5,6]

O(3N) = O(N)
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        ugly = [1]
        p2 = p3 = p5 = 0
    
        min_val = 0
        for _ in range(n-1):
            v2, v3, v5 = ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5
            min_val = min(v2, v3, v5)
    
            if min_val == v2:
                p2 += 1
    
            if min_val == v3:
                p3 += 1
    
            if min_val == v5:
                p5 += 1
            
            ugly.append(min_val)
        
        return min_val
    

s = Solution()
print(s.nthUglyNumber(10))
print(s.nthUglyNumber(11))
            
            
