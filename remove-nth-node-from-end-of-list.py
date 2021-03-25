"""
we only need n+1th and nth and n-1th node from the end
connect n+1th to n-1th node from the end
if n-1 th node does not exist, make n+1th node's next null
if n th node does not exist, do nothing

dummy 1 2 3 4 5
^       c
      ^   c
        ^   c
          ^   c
            ^   c
it doesn't work when [1,2], I couldn't know how to fix
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy = ListNode(next=head)
#         dummy.next = head
#         n_prev = dummy
#         n_node = head
#         n_next = head.next
# 
#         """
#         n_prev 1
#         n_node 2
#         n_next 2
# 
#         cur    1
#         n      0
#         """
# 
#         cur = dummy
#         while cur and n > 0:
#             cur = cur.next
#             n -= 1
# 
#         while cur and cur.next:
#             n_prev, n_node = n_node, n_next
#             n_next = cur.next
#             cur = cur.next
# 
#         if n <= 0:
#             n_prev.next = n_next
#         return dummy.next

"""
first pointer moves N step from the head
second pointer moves from the head
when first pointer gets to the end, second pointer is n steps behind from the last
prev.next = second.next

dummy,1,2,3,4,5 n=2
s       f 
            s   f

dummy,1  n=1                
s     f
      s f

d,1,2 n=1
s f
    s f

d,1,2 n=5 -> do nothing
s    f

time: O(N) space: O(1)
"""        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        
        first = dummy
        second = dummy
        
        while first and n > 0:
            first = first.next
            n -= 1
        
        if n > 0:
            return head
        
        prev = None
        while first:
            prev = second
            first = first.next
            second = second.next
        
        prev.next = second.next
        return dummy.next
