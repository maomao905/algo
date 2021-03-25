"""
we have 3 conditions to make triangle
a + b > c
b + c > a
c + a > b

if a <= b <= c, we only need to check a + b > c

- sort the array
- fix one element a
  we find the pairs that c - b < a is satisfied
- two pointers
  left pointer represents b, right pointer represents c
  3 4 5 6 7    a = 3
  b c          ok
  b   c
  b     c      x
    b   c      move pointer of b to right and add count = c - (b+1) because b=4, c=5 is also valid
    b     c    x
      b   c    move pointer of b to right and add count = c - (b+1)


O(N^2)
"""


from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        N=len(nums)
        cnt = 0
        for i in range(N-2):
            max_diff = nums[i]
            if nums[i] == 0:
                continue
            
            # we keep the difference between nums[k] - nums[j] within max_diff
            # and move pointer j, k forward
            """
            3 4 5 6 max_diff = 2
            j k      ok
            j   k    x  add (k-j-1)
              j k
            """
            j, k = i+1, i+2
            
            # O(N)
            for j in range(i+1, N):
                while k < N and nums[k] - nums[j] < max_diff:
                    k += 1
                cnt += k - j - 1
        return cnt

s = Solution()
# print(s.triangleNumber([0,1,1,1]))
# print(s.triangleNumber([2,2,3,4]))
print(s.triangleNumber([1,2,3,4,5,6]))
                
