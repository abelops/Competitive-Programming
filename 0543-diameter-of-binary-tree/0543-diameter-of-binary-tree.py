# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calcHeight(node):
            if not node:
                return 0
            return max(calcHeight(node.left), calcHeight(node.right)) + 1
        
        
        if not root:
            return 0
        
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        current = calcHeight(root.left) + calcHeight(root.right)
        
        return max(current, right, left)