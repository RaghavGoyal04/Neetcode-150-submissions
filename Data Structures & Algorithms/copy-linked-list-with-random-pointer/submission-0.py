"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = newLL = Node(-1)
        cur = head
        hm = {}
        while cur:
            node = Node(cur.val)
            dummy.next = node
            hm[cur] = node
            hm[node] = cur
            dummy, cur = dummy.next, cur.next

        dummy = newLL.next
        while dummy:
            dummy.random = None
            if hm[dummy] and hm[dummy].random:
                orig_rand_node = hm[dummy].random
                dummy.random = hm[orig_rand_node]
            dummy = dummy.next

        return newLL.next