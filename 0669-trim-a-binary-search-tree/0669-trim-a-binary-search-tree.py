# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(node):
            if not node:
                return None
            if node.val < low:
                node.left = None
                node = trim(node.right)
            elif node.val > high:
                node.right = None
                node = trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
            return node
        return trim(root)
            
                
            