"""
count zigzag point
/\ or \/

keep track of previous state (up or down) because they may be equal and we cannot know where is the last up/down state
time O(N) space O(1)
"""
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N=len(nums)
        ans = 1
        up = None
        for i in range(1, N):
            if nums[i] == nums[i-1]:
                continue
            if up is None or (nums[i] > nums[i-1]) ^ up:
                ans += 1
            up = nums[i] > nums[i-1]
        return ans

"""
DP

time O(N) space O(1)
"""
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N=len(nums)
        if N == 0:
            return 0
        
        up = 1 # previous up point's count
        down = 1 # previous down point's count
        for i in range(1, N):
            if nums[i-1] < nums[i]:
                up = down + 1
            elif nums[i-1] > nums[i]:
                down = up + 1
        
        return max(up, down)
    

s = Solution()
print(s.wiggleMaxLength([1,7,4,9,2,5]))
print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(s.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
print(s.wiggleMaxLength([1,9]))
print(s.wiggleMaxLength([51,226,208,165,202,286,190,212,219,271,36,245,20,238,238,89,105,66,73,9,254,206,221,237,203,33,249,253,150,102,57,249,203,10,123,178,85,203,35,276,129,116,37,163,99,142,187,249,134,77,217,298,29,127,174,115,122,178,12,80,122,76,16,41,115,84,104,121,127,40,287,129,9,172,112,51,40,135,205,53,259,196,248,5,123,184,209,130,271,42,18,143,24,101,10,273,252,50,173,80,119,129,45,257,299,78,278,78,190,215,284,129,200,232,103,97,167,120,49,298,141,146,154,233,214,196,244,50,110,48,152,82,226,26,254,276,292,286,215,56,128,122,82,241,222,12,272,192,224,136,116,70,39,207,295,49,194,90,210,123,271,18,276,87,177,240,276,33,155,200,51,6,212,36,149,202,48,114,58,91,83,221,175,148,278,300,284,86,191,95,77,215,113,257,153,135,217,76,85,269,126,194,199,195,20,204,194,50,220,228,90,221,256,87,157,246,74,156,9,196,16,259,234,79,31,206,148,12,223,151,96,229,165,9,144,26,255,201,33,89,145,155,1,204,37,107,80,212,88,186,254,9,158,180,24,45,158,100,52,131,71,174,229,236,296,299,184,168,41,45,76,68,122,85,292,238,293,179,143,128,47,87,267,53,187,76,292,0,160,70,172,292,9,64,156,153,26,145,196,222]))
print(s.wiggleMaxLength([3,3,3,2,5]))
print(s.wiggleMaxLength([0,0,0]))
print(s.wiggleMaxLength([1,1,7,4,9,2,5]))
