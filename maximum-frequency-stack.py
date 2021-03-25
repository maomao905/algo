"""
balanced binary tree

push/pop O(logN)
"""
from sortedcontainers import SortedList
from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.sl = SortedList() # (count, i, num)
        self.i = 0
        self.pos = defaultdict(list) # {num : list of i}

    def push(self, x: int) -> None:
        if self.pos[x]:
            pos = self.pos[x]
            item = (len(pos), pos[-1], x)
            self.sl.remove(item)
            item = (item[0]+1, self.i, x)
            self.sl.add(item)
            self.pos[x].append(self.i)
        else:
            self.sl.add((1,self.i, x))
            self.pos[x] = [self.i]
        self.i += 1

    def pop(self) -> int:
        item = self.sl.pop()
        x = item[2]
        self.pos[x].pop()
        
        if self.pos[x]:
            item = (item[0]-1, self.pos[x][-1], x)
            self.sl.add(item)
        return x

"""
necessary components
- frequency map {num: count}
- current maximum frequency
- maximum frequency map {frequency: [list of number]}

push 5,7,5,7,4,5
freq: {5:3}
max_freq: 3
max_freq_records: {1:[5,7,4],2:[5,7],3:[5]}
O(N)
"""
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.max_freq = 0
        self.max_freq_records = defaultdict(list)

    def push(self, x: int) -> None:
        self.freq[x] += 1
        freq = self.freq[x]
        if self.max_freq < freq:
            self.max_freq = freq
        self.max_freq_records[freq].append(x)

    def pop(self) -> int:
        n = self.max_freq_records[self.max_freq].pop()
        self.freq[n] -= 1
        if len(self.max_freq_records[self.max_freq]) == 0:
            self.max_freq -= 1
        return n

# Your FreqStack object will be instantiated and called as such:
fs = FreqStack()
for x in (5,7,5,7,4,5):
    fs.push(x)
for _ in range(4):
    print(fs.pop())
