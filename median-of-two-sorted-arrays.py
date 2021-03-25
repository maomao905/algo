"""
two pointers

calculate median indices beforehand
get the median values using two pointers

O(M+N)
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M,N=len(nums1),len(nums2)
        
        i = j = 0
        
        K=(M+N)//2
        median_idx = set([K]) if (M+N)%2 else set([K-1,K])
        medians = []
        
        total = 0
        i_turn = False
        while i < M or j < N:
            if i >= M:
                i_turn = False
            elif j >= N:
                i_turn = True
            elif nums1[i] < nums2[j]:
                i_turn = True
            else:
                i_turn = False
            
            cur = 0
            if i_turn:
                cur = nums1[i]
                i += 1
            else:
                cur = nums2[j]
                j += 1
                
            if total in median_idx:
                medians.append(cur)
            
            total += 1
        
        return sum(medians) / len(medians)

"""
binary search

1. M+N is even
Y = [1,3,6], Y = [2,5,9]

X 1 3 | 6     max_left_X = 3, min_right_X = 6
Y 2   | 5 9   max_left_Y = 2, min_right_Y = 5

when max_left_X <= min_right_Y and max_left_Y <= min_right_Y, it's a valid partition
median is (3 + 5) / 2 = (max(max_left_X, max_left_Y) + min(min_right_X, min_right_Y)) / 2

2. M+N is odd
X = [1,3,6], Y = [2,5,6,9]

X 1 3 | 6    max_left_X = 3, min_right_X = 6
Y 2 5 | 6 9  max_left_Y = 2, min_right_Y = 5

median is 5 = max(max_left_X, max_left_Y)

left partition nums = (M + N + 1) // 2 
(even) M=3,N=3 (3 + 3 + 1) // 2 = 3
(odd)  M=3,N=4 (3 + 4 + 1) // 2 = 4
the reason why plus 1 is we want to fix left partions nums > right partition nums

binary search to find the right partion of X and then partition of Y is automatically decided
X = [1,3,4,10], Y = [2,5,6,9]

mid of X is (0+4) // 2 = 2th index = 4
X 1 3 | 4 10
Y 2 5 | 6 9        max_left_Y (5) > min_right_X(4) -> mid should be right of X

mid of X is (2+4) // 2 = 3th index
X 1 3 4 | 10
Y 2     | 5 6 9      valid

median is (max(4, 2) + min(10, 5)) / 2 = (4 + 5) / 2 = 4.5

O(log(min(M,N)))
"""

class Solution:
    def get_val(self, nums, i):
        if i < 0:
            return float('-inf')
        elif i >= len(nums):
            return float('inf')
        else:
            return nums[i]
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M,N=len(nums1),len(nums2)
        if M == 0:
            mid = N//2
            return nums2[mid] if N%2 else (nums2[mid] + nums2[mid-1])/2
        elif N == 0:
            mid = M//2
            return nums1[M//2] if M%2 else (nums1[mid] + nums1[mid-1])/2
        
        left_nums = (M+N+1) // 2
        
        l,r = 0,M
        
        max_left_X = min_right_X = max_left_Y = min_right_Y = 0
        while l <= r:
            mid = l+(r-l)//2
            mid_Y = left_nums - mid
            max_left_X = self.get_val(nums1, mid-1)
            min_right_X = self.get_val(nums1, mid)
            
            max_left_Y = self.get_val(nums2, mid_Y-1)
            min_right_Y = self.get_val(nums2, mid_Y)
            # print('mid',mid, 'mid_Y',mid_Y, 'max_left_X',max_left_X, 'min_right_X',min_right_X,'max_left_Y',max_left_Y,'min_right_Y',min_right_Y)
            if max_left_X > min_right_Y:
                r = mid-1
            elif min_right_X < max_left_Y:
                l = mid+1
            else:
                if (M+N) % 2:
                    return max(max_left_X, max_left_Y)
                else:
                    return (max(max_left_X, max_left_Y) + min(min_right_X, min_right_Y)) / 2
        
            

s = Solution()
print(s.findMedianSortedArrays([1,3], [2]))
print(s.findMedianSortedArrays([1,2], [3,4]))
print(s.findMedianSortedArrays([0,0],[0,0]))
print(s.findMedianSortedArrays([],[1]))
print(s.findMedianSortedArrays([],[2]))
print(s.findMedianSortedArrays([],[2,3]))
print(s.findMedianSortedArrays([3],[-2,-1]))
print(s.findMedianSortedArrays([1],[2,3]))
