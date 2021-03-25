# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1 -> 2 -> 3 -> 3 -> 3 -> 4

1 next 2 next.next 3 -> 2 != 3 -> move to next node
2 next 3 next.next 3 -> 3 == 3 -> while next == next.next: move to next node
  next 3 next.next 3 -> 3 == 3
  next 3 next.next 4 -> 3 != 4 -> 2's next is 4
if next is None -> end
if next.next is None -> move to next node

prev dummy -> head(1) -> 2
cur head(1) -> 2 -> 3 -> 3 -> 3

time: O(N)      
space: O(1)
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(next=head)
        
        prev = dummy
        cur = head
        while cur:
            # cur is 3 and cur.next is 3
            if cur.next and cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
            
            cur = cur.next
        
        return dummy.next

        
        
