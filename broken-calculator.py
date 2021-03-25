"""
think from Y to X
O(logY)
"""
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X > Y:
            return X-Y
        
        ans = 0
        while X < Y:
            if Y%2:
                Y+=1
            else:
                Y//=2
            ans += 1
        return ans + Y-X

s = Solution()
print(s.brokenCalc(2,3))
print(s.brokenCalc(5,8))
print(s.brokenCalc(3,10))
print(s.brokenCalc(1024,1))
                
                
