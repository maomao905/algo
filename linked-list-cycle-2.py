# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
k is the start of loop
- create slow and fast pointer
- slow and fast pointer meet at k + (loop_size - k)
    - when slow enter the loop, fast pointer is k steps from the start of loop,
      which means fast pointer is loop_size - k steps behind the slow pointer.
    - fast pointer get one step closer each time, so they will meet after loop_size - k steps
    - if k > loop_size: they will meet at loop_size - mod(k, loop_size) steps
- move slow pointer to the head of linked list and fast pointer stays where it is,
  they take one step at the same time and where they collide is the start of loop


time: O(n)
space: O(1)
"""

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if fast is None or fast.next is None:
            return None
        
        slow = head
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
        
        
        
