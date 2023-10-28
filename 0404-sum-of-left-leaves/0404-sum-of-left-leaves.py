# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        tot = 0
        def dfs(node, d):
            nonlocal tot
            if node:
                if not node.left and not node.right:
                    if d == "l":
                        tot+=node.val
                    return []
                if node.right:
                    dfs(node.right, "r")
                if node.left:
                    dfs(node.left, "l")
        dfs(root, "")
        return tot
            