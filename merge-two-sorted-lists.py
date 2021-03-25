"""
3 pointers in total
ptr: pointer of new sorted list
first: pointer of first linked list
second: pointer of second linked list

dummy head

1 -> 2 -> 4

1 -> 3 -> 4

ptr    first  second
dummy   1     1
1       2     1
1       2     3
2       4     4
4       None  4
4       None  None

time: O(L1+L2)
space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        
        ptr = dummy
        
        while l1 and l2:
            if l1.val > l2.val:
                ptr.next = l2
                l2 = l2.next
            else:
                ptr.next = l1
                l1 = l1.next
            ptr = ptr.next
        
        ptr.next = l1 or l2
        
        return dummy.next
