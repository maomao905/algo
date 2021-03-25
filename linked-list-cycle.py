# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# head = [3,2,0,-4]
# save the already passed nodes [3, 2, 0, -4]
# 3,2,0,-4
# 2,-4,0
# O(n)
# O(n)
# runner-technique
# first pointer one step ahead
# second pointer two steps ahead
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
