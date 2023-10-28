# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preOrd(node):
            if not node:
                return [None]
            return [node.val] + preOrd(node.left) + preOrd(node.right)
        n1 = preOrd(p)
        n2 = preOrd(q)
        
        if n1 == n2:
            return True
        return False
        