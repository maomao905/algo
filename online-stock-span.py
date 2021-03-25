"""
monotonically decreasing stack

time O(N) space O(N)
"""

class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        cnt = 0
        while self.stack and self.stack[-1][0] <= price:
            _, span = self.stack.pop()
            cnt += span
        
        self.stack.append((price, cnt + 1))
        return self.stack[-1][1]
        


# Your StockSpanner object will be instantiated and called as such:
s = StockSpanner()
print(s.next(100))
print(s.next(80))
print(s.next(80))
print(s.next(70))
print(s.next(60))
print(s.next(75))
print(s.next(85))
