"""
4,2,1,3
2,1,3,4

bubble sort O(N^2)

NlogN -> merge sort, quick sort

merge sort
4 2 1 3
2 4 1 3
1 4 1 3
1 2 1 3
1 2 3 3
1 2 3 4

how to know where the second pointer starts
 -> two pointers (slow and fast)

time: O(NlogN)
space: O(logN) for recursion stack
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head):
        slow = None
        fast = head
        
        while fast and fast.next:
            slow = head if slow is None else slow.next
            fast = fast.next.next
        
        second = slow.next
        # make partition end null for merge sort
        slow.next = None
        return second
    
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

        
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        second = self.partition(head)
        
        return self.mergeTwoLists(self.sortList(head), self.sortList(second))


def make(arr):
    dummy = ListNode()
    cur = dummy
    i = 0
    while i < len(arr):
        cur.next = ListNode(arr[i])
        cur = cur.next
        i += 1
    return dummy.next

def debug(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)
        
s = Solution()    
debug(s.sortList(make([4,2,1,3])))
debug(s.sortList(make([-1,5,3,4,0])))
