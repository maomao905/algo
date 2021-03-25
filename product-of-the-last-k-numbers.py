"""
cumulative product
keep track of last zero position
last k includes last zero position, return 0
"""

class ProductOfNumbers:

    def __init__(self):
        self.C = [1]
        self.last_zero = -1
        
    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero = len(self.C)
        self.C.append(max(self.C[-1],1) * num)
        # print(self.C, self.last_zero)
        
    def getProduct(self, k: int) -> int:
        # 6 - 4 < 2
        if len(self.C) - k <= self.last_zero:
            return 0
        return self.C[-1]//max(self.C[-k-1], 1)
        


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
obj.add(8)
print(obj.getProduct(2))
