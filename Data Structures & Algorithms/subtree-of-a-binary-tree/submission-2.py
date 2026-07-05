# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root, subRoot):
        # If either is None, both must be None to be equal.
        if not root or not subRoot:
            return root is subRoot

        return (
            root.val == subRoot.val
            and self.isSameTree(root.left, subRoot.left)
            and self.isSameTree(root.right, subRoot.right)
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        return (self.isSameTree(root, subRoot) 
            or self.isSubtree(root.left, subRoot) 
            or self.isSubtree(root.right, subRoot)
        )