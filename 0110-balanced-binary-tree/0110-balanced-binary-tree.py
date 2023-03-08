# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        temp = 0
        def trav(node):
            nonlocal temp
            if not node:
                return 0
            l = trav(node.left) 
            r = trav(node.right)
            temp = max(temp, abs(r-l))
            return max(l, r) + 1
        trav(root)
        if temp > 1:
            return False
        return True