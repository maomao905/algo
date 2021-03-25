"""
self.tree[1] = nums[0]
self.tree[2] = nums[0] + nums[1]
self.tree[3] = nums[2]
self.tree[4] = nums[0] + nums[1] + nums[2] + nums[3]
self.tree[5] = nums[4]
self.tree[6] = nums[4] + nums[5]
self.tree[7] = nums[6]
self.tree[8] = nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7]
"""
class BIT():
    def __init__(self, nums):
        self.nums = nums
        self.N = len(nums)
        self.tree = [0] * (self.N+1)
        
        for i in range(self.N):
            j = i + 1
            while j <= self.N:
                self.tree[j] += nums[i]
                j += j & -j
        
    def update(self, i, val):
        diff, self.nums[i] = val - self.nums[i], val
        i += 1
        while i <= self.N:
            self.tree[i] += diff
            i += i & -i
    
    def prefix_sum(self, i):
        _sum = 0
        i += 1
        while i:
            _sum += self.tree[i]
            i -= i & -i
        return _sum
    
    def range_sum(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i-1)
        
arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
tree = BIT(arr)
print(tree.prefix_sum(2))
print(tree.range_sum(2,8))
tree.update(3,20)
print(tree.range_sum(2,8))
