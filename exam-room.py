import heapq
class ExamRoom:
    def dist(self, x, y):
        if x == -1:
            return -y
        elif y == self.N:
            return self.N - 1 - x
        else:
            return -abs(x-y)//2

    def __init__(self, N: int):
        self.q = [self.dist(-1,N)]

    def seat(self) -> int:
        

    def leave(self, p: int) -> None:
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
