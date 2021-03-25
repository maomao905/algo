from typing import List

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = [-1] * (10 ** 6)
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.h[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.h[key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.h[key] = -1

"""
hash function using modulo
- use arbitary number as modulo
- if conflicted, iterate the bucket (linked list is also possible)

using linkedlist, removal operation takes O(1), while using array, removal takes O(N), but I just filled -1 
"""
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 2000
        self.h = [[] for _ in range(self.mod)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        m = key%self.mod
        for i, (k, v) in enumerate(self.h[m]):
            if key == k:
                self.h[m][i] = (key, value)
                return
        self.h[m].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for k, v in self.h[key%self.mod]:
            if key == k:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        m = key%self.mod
        for i, (k, v) in enumerate(self.h[m]):
            if key == k:
                self.h[m][i] = (k, -1)
        


# Your MyHashMap object will be instantiated and called as such:
h = MyHashMap()
h.put(1,1)
h.put(2,2)
h.put(4904, 6)
print(h.get(1))
print(h.get(3))
h.put(2,1)
print(h.get(2))
h.remove(2)
print(h.get(2))
print(h.get(4904))
print(h.h)
