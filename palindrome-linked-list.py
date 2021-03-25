# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
1->2->2->1
1,2,3,2,1
1,2,3,2,3,3,2,3,2,1

palindrome characteristics
- prev center next
    - prev == next
- two pointers
    - when fast pointer reaches the end, slow pointer should be at center
    
    1221 f 4 s 2 -> ok 12, 21
    12321 f 5(6) s 3 -> ok 12, 21
    - use stack to reverse O(N) space
    - change next pointer (reverse pointer) O(1) space, O(N) time
        - 1 -> 2 -> 3
        - 1 <- 2 <- 3
        prev None
        cur 1
        1.next = 2 -> None(prev)
        
        prev 1
        cur 2
        2.next = 3 -> 1(prev)
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        # identify the center using two pointers
        slow = fast = head
        
        """
          1,2,3,3,2,1 (even)
        s ^ ^ ^ ^
        f ^   ^   ^  ^
        reverse 3 <- 2 <- 1 ok
        
          1,2,3,2,1 (odd)
        s ^ ^ ^
        f ^   ^   ^
        reverse 3 <- 2 <- 1 need to move one step forward
        """
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        is_odd = fast is not None
        if is_odd:
            slow = slow.next
        
        """
        3 -> 2 -> 1
        3 <- 2 <- 1
        
        backward: 2
        next: 1
        backward.next = 3
        prev = 2
        backward = 1
        """
        # reverse the second half
        backward = slow
        prev = None
        while backward.next:
            next = backward.next
            backward.next = prev
            prev = backward
            backward = next
        backward.next = prev
        
        # compare backward and forward from the center
        while backward:
            # print(forward.val, backward.val)
            if head.val != backward.val:
                return False
            head = head.next
            backward = backward.next
        
        return True


def create_test_data(arr):
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

s = Solution()

head = create_test_data([1,2,2,1])
print(s.isPalindrome(head))
head = create_test_data([1,2,3,2,1])
print(s.isPalindrome(head))
head = create_test_data([1,2,3,2,1,2])
print(s.isPalindrome(head))
head = create_test_data([1,2])
print(s.isPalindrome(head))
head = create_test_data([1,0,0])
print(s.isPalindrome(head))
head = create_test_data([1])
print(s.isPalindrome(head))
