"""
space O(N)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = []
        large = []
        
        cur = head
        while cur:
            if cur.val < x:
                small.append(cur)
            else:
                large.append(cur)
            cur = cur.next

        dummy = ListNode()
        
        cur = dummy
        for node in small:
            cur.next = node
            cur = cur.next
        
        for node in large:
            cur.next = node
            cur = cur.next
            cur.next = None
        
        return dummy.next

"""
space O(1)
"""
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = dummy1 = ListNode()
        large = dummy2 = ListNode()
        
        cur = head
        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                large.next = cur
                large = large.next
            cur = cur.next
        
        large.next = None
        small.next = dummy2.next
        return dummy1.next
