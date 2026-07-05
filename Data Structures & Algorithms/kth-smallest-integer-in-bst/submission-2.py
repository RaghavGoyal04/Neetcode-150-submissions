# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # minHeap = []
        # def dfs(root):
        #     if not root: return
        #     heapq.heappush(minHeap, root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # for i in range(len(minHeap)):
        #     temp = heapq.heappop(minHeap)
        #     if i == k-1:
        #         return temp

        # maxHeap = []
        # def dfs(root):
        #     if not root: return
        #     heapq.heappush(maxHeap, -root.val)
        #     if len(maxHeap) > k:
        #         heapq.heappop(maxHeap)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return -maxHeap[0]

        ans, count = None, 0
        def dfs(root):
            nonlocal count, ans
            if not root or ans is not None: return
            
            dfs(root.left)
            
            if ans is not None:   # stop if already found in left subtree
                return

            count += 1
            if count == k:
                ans = root.val
                return

            dfs(root.right)
        dfs(root)
        return ans


        