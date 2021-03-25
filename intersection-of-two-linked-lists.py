"""
if both A and B have the same distance to intersection, they merge at intersection
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_size(self, node):
        size = 0
        while node:
            node = node.next
            size += 1
        return size
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        sizeA = self.get_size(headA)
        sizeB = self.get_size(headB)
        
        if sizeA > sizeB:
            for _ in range(sizeA - sizeB):
                headA = headA.next
        else:
            for _ in range(sizeB - sizeA):
                headB = headB.next
        
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None

"""
simpler solution with same logic

when there is no intersection, a and b are None and return None
"""            
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:        
        if not headA or not headB:
            return None
        
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
