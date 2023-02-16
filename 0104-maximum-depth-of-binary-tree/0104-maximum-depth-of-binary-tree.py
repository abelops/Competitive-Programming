# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, root, d):
        if not root:
            return d
        return max(self.DFS(root.left, d+1), self.DFS(root.right, d+1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root, 0)