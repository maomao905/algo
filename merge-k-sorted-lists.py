"""
n: number of total elements
k: number of linked lists
time: O(nlogk)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # in order to compare the same value, we store index in heap, otherwise runtime error
        heap = [(l.val, idx, l) for idx, l in enumerate(lists) if l is not None]
        heapify(heap)
        
        dummy = ListNode()
        cur = dummy
        while heap:
            _, idx, node = heappop(heap)
            next_node = node.next
            if next_node:
                heappush(heap, (next_node.val, idx, next_node))
            cur.next = node
            cur = node
        return dummy.next
