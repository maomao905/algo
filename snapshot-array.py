"""
store the snap id and value of the same index in the same array
binary search snap id of particular index
[
  [(snap_id1, val1),(snap_id3,val3)],
  [],
  [],
  ...
]

init O(N)
set O(1)
snap O(1)
get O(logS) S: number of snaps
"""

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(-1,0)] for _ in range(length)]
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        arr = self.arr[index]
        if len(arr) == 0:
            return 0
        
        l,r = 0, len(arr)
        while l<r:
            mid = l + (r-l)//2
            if arr[mid][0] <= snap_id:
                l = mid + 1
            else:
                r = mid
        # we want the last value of the same snap id, thus l-1
        return arr[l-1][1]

# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(2)
print(obj.snap())
print(obj.get(1,0))
print(obj.get(0,0))
obj.set(1,8)
print(obj.get(1,0))
obj.set(0,20)
print(obj.get(0,0))
obj.set(0,7)
