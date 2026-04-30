# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        
        #find middle
        while f and f.next:
            s, f = s.next, f.next.next
        another_half, s.next = s.next, None
        
        #reverse the other half
        prev, rev = None, another_half
        while rev:
            rev.next, prev, rev = prev, rev, rev.next

        #join
        cur = head
        while cur and prev:
            # print(cur.val, prev.val)
            temp1, temp2 = cur.next, prev.next
            cur.next = prev
            prev.next = temp1
            cur = temp1
            prev = temp2
        
            