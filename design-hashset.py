# https://leetcode.com/problems/design-hashset/

M = 100001

def h1(key):
    return key % M

def h2(key):
    return 1 + (key % (M - 1))

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.hash_table = [None] * M
        

    def add(self, key: int) -> None:
        i = 1
        h = h1(key)
        while self.hash_table[h] != key:
            if self.hash_table[h] is None:
                self.hash_table[h] = key
                return
            h = (h + i * h2(key)) % M
            i += 1
        

    def remove(self, key: int) -> None:
        i = 1
        h = h1(key)
        while self.hash_table[h] is not None:
            if self.hash_table[h] == key:
                self.hash_table[h] = None
                return
            h = (h + i * h2(key)) % M
            i += 1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = 1
        h = h1(key)
        while self.hash_table[h] is not None:
            if self.hash_table[h] == key:
                return True
            h = (h + i * h2(key)) % M
            i += 1
        return False
        


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
key=0
obj.add(key)
# obj.remove(key)
param_3 = obj.contains(key)
print(param_3)
