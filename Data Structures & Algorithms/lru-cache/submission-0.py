class Node:
    def __init__(self, key=0, val=0, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:
    def __init__(self, capacity: int):
        self.LRU = {}
        self.head = Node()
        self.tail = Node()
        self.head.right, self.tail.left = self.tail, self.head
        self.capacity = capacity
        self.length = 0

    def add_in_front(self, node):
        temp = self.head.right
        node.left, node.right = self.head, self.head.right
        self.head.right, temp.left = node, node
        self.length += 1
    
    def remove(self, node):
        node.left.right, node.right.left = node.right, node.left
        self.length -= 1

    def get(self, key: int) -> int:
        if key not in self.LRU:
            return -1

        node = self.LRU[key]
        self.remove(node)
        self.add_in_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            self.remove(self.LRU[key])
        
        node = Node(key, value)
        self.add_in_front(node)
        self.LRU[key] = node

        if self.length > self.capacity:
            to_be_deleted = self.tail.left
            self.remove(to_be_deleted)
            del self.LRU[to_be_deleted.key]
        

            




