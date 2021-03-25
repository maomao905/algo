"""
store element in array and store the value and index in hash map

{1:0,3:1,4:2}
[1,3,4] when 1 is removed, swap with the last element [4,3,1] then pop last element
update the hash map as well {4:0,3:1}
insert [1,3,5] {4:0,3:1,5:2}
getRandom -> randomly get index, then we can get value

time O(1)
space O(N)
"""
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.m = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.m:
            i = len(self.nums)
            self.m[val] = i
            self.nums.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.m:
            return False
        
        i = self.m[val]
        # swap with last element
        self.nums[i], self.nums[-1] = self.nums[-1], self.nums[i]
        self.m[self.nums[i]] = i
        self.nums.pop()
        del self.m[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        i = random.randint(0,len(self.nums)-1)
        return self.nums[i]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())
