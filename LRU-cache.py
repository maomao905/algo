"""
queue [1,2]
put 1 [1]
put 2 [1,2]
get 1 [2,1] remove 1 and put 1

queue: remove takes O(N) and append O(1)
linked hash map: remove O(1), append O(1), get O(1)
"""
from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self:
            self[key] = value
            self.move_to_end(key)
        else:
            if len(self) >= self.capacity:
                self.popitem(last=False)
            self[key] = value

"""
hash map + double linked list
hash mapのkeyにはkeyをvalueにはdouble linked listのnodeのpointerを入れておく
double linked listはremoveはO(1), addもO(1)
getはhash mapから探すのでO(1)
spaceはO(capacity)
"""
class Node:
    def __init__(self, prev=None, next=None, key=None, value=None):
        self.prev = prev
        self.next = next
        self.key = key
        self.value = value

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add(self, node):
        # print('^^^^^^', node.key, node.value)
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def pop(self):
        prev = self.tail.prev
        prev_prev = prev.prev
        prev_prev.next = self.tail
        self.tail.prev = prev_prev
        return prev.key
    # def remove(self, key):
    def move_to_head(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.add(node)
        
    def _print(self):
        cur = self.head
        while cur is not None:
            print(cur.key, cur.value)
            cur = cur.next

class LRUCache:
    def __init__(self, capacity: int):
        self.ht = {}
        self.dl = DoubleLinkedList()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key in self.ht:
            # move node to head
            node = self.ht[key]
            self.dl.move_to_head(node)
            return node.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.ht:
            node = self.ht[key]
            node.value = value
            # move node to head
            self.dl.move_to_head(node)
        else:
            if len(self.ht) >= self.capacity:
                # pop last item from doubly linked list
                tail_key = self.dl.pop()
                # remove from hash map
                del self.ht[tail_key]
            # add to double linked list
            node = Node(key=key, value=value)
            self.dl.add(node)
            # add to hash map
            self.ht[key] = node


# Your LRUCache object will be instantiated and called as such:
capacity=2
cache = LRUCache(capacity)
print(cache.put(1,1))
print(cache.put(2,2))
print(cache.get(1))
print(cache.put(3,3))
print(cache.get(2))
print(cache.put(4,4))
