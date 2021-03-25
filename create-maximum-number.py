"""
(WA)
1. sort the nums1 and nums2
2. we want the largest number that appear later and satisfy k (we still have k numbers available even if we choose the number)

time
1. sort O((M+N)log(M+N))
2. O(k*(M+N))
    if k == (M+N): (M+N)^2
space O(M+N)

the case below does not work (when there is a same number and same i1 and i2 and we need to know which array we should choose)
nums1=[8,9],nums2[3,9] k=3
"""
from typing import List
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        nums = [(n,i,0) for i, n in enumerate(nums1)] + [(n,i,1) for i, n in enumerate(nums2)]
        nums.sort(key=lambda x: (-x[0],x[1],x[2]))
        # print(nums)
        M,N=len(nums1),len(nums2)
        seen = set()
        res = [0] * k
        i1,i2 = -1,-1
        for _k in range(k):
            for n,i,j in nums:
                if (n,i,j) in seen:
                    continue
                if (j == 0 and i < i1) or (j==1 and i<i2):
                    continue
                
                if j==0 and (M-i + N-i2-1 >= k-_k):
                    res[_k] = n
                    seen.add((n,i,j))
                    i1 = i
                    break
                if j==1 and (N-i + M-i1-1 >= k-_k):
                    res[_k] = n
                    seen.add((n,i,j))
                    i2 = i
                    break
        return res

"""
1. m nums from nums1 and n nums from nums2 where m + n = k
  process all pairs of <m,n>
2. get m maximum nums from nums1 and get n maximum nums from nums2
  stack
3. merge m and n
  two pointers

O(k*(M+N))
"""            
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def get_max_nums(nums, k):
            # print('k',k)
            _k = k
            stack = []
            if k == 0:
                return stack
            for i in range(len(nums)):
                remain = len(nums) - i
                # print(i,nums, remain,k)
                while stack and nums[i] > stack[-1] and k < remain:
                    stack.pop()
                    k += 1
                if k > 0:
                    stack.append(nums[i])
                    k -= 1
            assert len(stack) == _k, print(len(stack), _k)
            return stack
        
        def merge(A, B):
            res = []
            i,j = 0,0
            while i < len(A) and j < len(B):
                if A[i] > B[j]:
                    res.append(A[i])
                    i += 1
                else:
                    res.append(B[j])
                    j += 1
            
            if i < len(A):
                res.extend(A[i:])
            elif j < len(B):
                res.extend(B[j:])
            return res
        
        def update_maximum(nums):
            nonlocal ans
            if not ans:
                ans = nums
                return
            for i,j in zip(ans, nums):
                if i > j:
                    return
                elif i < j:
                    ans = nums
        
        ans = []
        for i in range(k):
            if i > len(nums1) or k-i > len(nums2):
                continue
            max_nums1 = get_max_nums(nums1, i)
            max_nums2 = get_max_nums(nums2, k-i)
            print(max_nums1,max_nums2)
            max_nums = merge(max_nums1, max_nums2)
            # print(max_nums)
            update_maximum(max_nums)
        return ans
        
            
s = Solution()
# print(s.maxNumber([3,4,6,5],[9,1,2,5,8,3],5))
print(s.maxNumber([6,7],[6,0,4],5))
# print(s.maxNumber([3,9],[8,9],3))
        
