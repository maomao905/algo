class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cnt = Counter()
        for i, n in enumerate(nums):
            cnt[n] += 1
            if i > k:
                cnt[nums[i-k-1]] -= 1
                
            if cnt[n] > 1:
                return True
        return False
