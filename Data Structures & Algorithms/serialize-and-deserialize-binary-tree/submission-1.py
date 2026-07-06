# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # if not root: return 'N'
        # res = []
        # q = deque([root])
        # while q:
        #     node = q.popleft()
        #     if not node:
        #         res.append("N")
        #     else:
        #         res.append(str(node.val))
        #         q.append(node.left)
        #         q.append(node.right)
        # print(",".join(res))
        # return ",".join(res)


        res = []
        def dfs(root):
            if not root :
                res.append('N') 
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        print(root)
        return ','.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # vals = data.split(',')
        # if vals[0] == 'N': return
        # root = TreeNode(vals[0])
        # queue = deque([root])
        # index = 1
        # while queue:
        #     node = queue.popleft()
        #     if vals[index] != 'N':
        #         node.left = TreeNode(int(vals[index]))
        #         queue.append(node.left)
        #     index += 1
        #     if vals[index] != "N":
        #         node.right = TreeNode(int(vals[index]))
        #         queue.append(node.right)
        #     index += 1
        # return root
        
        vals = data.split(',')
        self.i = 0
        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return 
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

