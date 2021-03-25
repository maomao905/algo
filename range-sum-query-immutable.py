from itertools import accumulate
class NumArray:

    def __init__(self, nums: List[int]):
        self.C = [0] + list(accumulate(nums))
        

    def sumRange(self, i: int, j: int) -> int:
        return self.C[j+1] - self.C[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
