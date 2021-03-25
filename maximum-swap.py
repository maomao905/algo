"""
swap the largest number that is larger than current number appearing later
O(N)
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(n) for n in str(num)]
        N=len(nums)
        
        back = [0] * N
        back[-1] = N-1
        for i in reversed(range(N-1)):
            if nums[i] > nums[back[i+1]]:
                back[i] = i
            else:
                back[i] = back[i+1]
        
        for i in range(N):
            if nums[i] < nums[back[i]]:
                nums[i], nums[back[i]] = nums[back[i]], nums[i]
                break
        return int(''.join([str(n) for n in nums]))

s = Solution()
print(s.maximumSwap(98689))
print(s.maximumSwap(986579))
print(s.maximumSwap(1993))
