# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = float("inf")
        def dfs(node, prev):
            nonlocal ans
            if node:
                if not node.left and not node.right:
                    ans = min(ans, prev+1)
                    return
                if node.left:
                    left = dfs(node.left, prev+1)
                if node.right:
                    right = dfs(node.right, prev+1)
        dfs(root, 0)
        
        return ans if root else 0