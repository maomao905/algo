from threading import Lock
class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0] * k
        self.i = 0
        self.size = 0
        self.lock = Lock()

    def enQueue(self, value: int) -> bool:
        with self.lock:
            if self.size == len(self.arr):
                return False
            self.arr[self.i] = value
            self.i = (self.i+1) % len(self.arr)
            self.size += 1
        return True

    def deQueue(self) -> bool:
        with self.lock:
            if self.isEmpty():
                return False
            self.arr[self.i - self.size] = -1
            self.size -= 1
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.i - self.size]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.i-1]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.arr)
        


myCircularQueue = MyCircularQueue(3);
print(myCircularQueue.enQueue(1)); # return True
print(myCircularQueue.enQueue(2)); # return True
print(myCircularQueue.enQueue(3)); # return True
print(myCircularQueue.enQueue(4)); # return False
print(myCircularQueue.Rear());     # return 3
print(myCircularQueue.isFull());   # return True
print(myCircularQueue.deQueue());  # return True
print(myCircularQueue.enQueue(4)); # return True
print(myCircularQueue.Rear());     # return 4
