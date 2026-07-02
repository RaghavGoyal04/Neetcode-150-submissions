# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_dfs(root):
            if not root: return 0
            return 1 + max(height_dfs(root.left), height_dfs(root.right))
        
        if not root: 
            return True

        lh = height_dfs(root.left)
        rh = height_dfs(root.right)
        
        #at any point the diff becomes larger than 1 return false
        if abs(lh-rh) > 1: return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)



