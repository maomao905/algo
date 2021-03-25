# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
iterative approach
time O(n) space O(1)
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        while current != None:
            next = current.next
            # reverse pointer
            current.next = prev

            # update
            prev = current
            current = next

        return prev

"""
recursive approach
time O(n) space O(n)
"""
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None: # head=5, head.next=None
#             return head # 5
#         node = self.reverseList(head.next) # head=4, head.next=5, node=5
#         head.next.next = head # 5のnextを4に
#         head.next = None # 4のnextはemptyに
#         return node # return the end of the linked list, which becomes head
    

s = Solution()
n5 = ListNode(5)
n4 = ListNode(4,n5)
n3 = ListNode(3,n4)
n2 = ListNode(2,n3)
n1 = ListNode(1,n2)

n = s.reverseList(n1)
print(n.val, n.next.val) # val=5, next=4

            
