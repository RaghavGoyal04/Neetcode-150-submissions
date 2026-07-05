# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        res = [0]
        def dfs(root, maxSoFar):
            if not root: return
            if root.val >= maxSoFar:
                res[0] += 1
                maxSoFar = root.val
            dfs(root.left, maxSoFar)
            dfs(root.right, maxSoFar)
        dfs(root, -101)
        return res[0]
        