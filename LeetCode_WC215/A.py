from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.arr = [""] * n
        self.ptr = 0
        self.n = n
        
    def insert(self, id: int, value: str) -> List[str]:
        self.arr[id-1] = value
        result = []
        while self.ptr < self.n:
            v = self.arr[self.ptr]
            if v == "":
                break
            
            result.append(v)
            self.ptr += 1
        return result
            
            
os= OrderedStream(5);
os.insert(3, "ccccc"); # Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa"); # Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb"); # Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee"); # Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); # Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
