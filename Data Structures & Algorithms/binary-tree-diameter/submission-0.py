# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            lh = dfs(root.left)
            rh = dfs(root.right)
            # we should not add 1 + lh + rh as we are counting edges for diameter not nodes
            self.res = max(lh+rh, self.res)
            # +1 because we want to return height/depth to current node's parent
            return 1 + max(lh, rh)

        dfs(root)
        return self.res

        