# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def dfs(root, lb, rb):
            if not root: 
                return True
            if lb < root.val < rb :
                return dfs(root.left, lb, root.val) and dfs(root.right, root.val, rb)
            return False
        return dfs(root, float('-inf'), float('inf'))


        