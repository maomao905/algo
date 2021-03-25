"""
1 -> 1 -> 1 -> 2
time: O(N)
space: O(1)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur is not None:
            ne = cur.next
            while ne is not None and cur.val == ne.val:
                ne = ne.next
            
            cur.next = ne
            cur = ne
        return head
            
        
