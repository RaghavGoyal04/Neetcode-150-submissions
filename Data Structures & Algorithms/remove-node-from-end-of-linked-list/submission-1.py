# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return
        
        dummy = ListNode(-1, head)
        left, right = dummy, head
        while n > 0 and right:
            n -= 1
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        
        # prev, cur = None, head
        # while cur:
        #     cur.next, prev, cur = prev, cur, cur.next
        
        # if n == 1:
        #     reversed_head = prev.next
        #     old_head, cur = None, reversed_head
        #     while cur:
        #         cur.next, old_head, cur = old_head, cur, cur.next
        #     return old_head
        # else:
        #     reversed_head = cur = prev
        #     cnt = 1
        #     while cnt != n-1:
        #         cur = cur.next
        #         cnt += 1 
        #     cur.next = cur.next.next

        #     old_head, cur = None, reversed_head
        #     while cur:
        #         cur.next, old_head, cur = old_head, cur, cur.next
        #     return old_head
        
        