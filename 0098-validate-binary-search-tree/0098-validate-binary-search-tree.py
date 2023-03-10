# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrd(node):
            if not node:
                return []
            return inOrd(node.left) + [node.val] + inOrd(node.right)
        ans = inOrd(root)
        if len(set(ans)) != len(ans):
            return False
        if sorted(ans) == ans:
            return True
        
        return False