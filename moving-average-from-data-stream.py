class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.k = size
        self.q = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        if len(self.q) > self.k:
            self.sum -= self.q.popleft()
        return self.sum / len(self.q)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
