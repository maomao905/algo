"""
lazy update
- store increment array
- when popping, we update increment array as well inc[-2] += inc[-1]
"""

class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if self.max_size <= len(self.stack):
            return
        self.stack.append(x)
        self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        n = self.inc.pop()
        if self.inc:
            self.inc[-1] += n
        return self.stack.pop() + n
        
    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.stack))-1] += val


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(1)
obj.push(2)
print(obj.pop())
obj.push(2)
obj.push(3)
obj.push(4)
obj.increment(5,100)
obj.increment(2,100)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
