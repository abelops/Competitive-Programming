# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(leftSide, rightSide):
            if (not leftSide and rightSide) or (leftSide and not rightSide):
                return False
            if not leftSide and not rightSide:
                return True
            if leftSide.val != rightSide.val:
                return False
            left = check(leftSide.left, rightSide.right)
            right = check(rightSide.left, leftSide.right)
            
            return left and right
            
        return check(root.left, root.right)
                