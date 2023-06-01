# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dp(node, memo):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            if node in memo:
                return memo[node]
            
            x, y = node.val, 0
            if node.left:
                x += dp(node.left.left, memo) + dp(node.left.right, memo)
                y+= dp(node.left, memo)
            if node.right:
                x+=dp(node.right.left, memo) + dp(node.right.right, memo)
                y+=dp(node.right, memo)
            memo[node] = max(x, y)
            return memo[node]
        return dp(root, {})