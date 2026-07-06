# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root: return 0
            left_sum = max(0, dfs(root.left))
            right_sum = max(0, dfs(root.right))
            # update global result with the best path through node
            res[0] = max(res[0], root.val + left_sum + right_sum)
            # return best downward path to the parent
            return root.val + max(left_sum, right_sum)
        dfs(root)
        return res[0]
        