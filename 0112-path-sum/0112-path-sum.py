# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def recur(s, node, prev):
            # if node:
            #     print(s, node.val)
            if not node and (prev and not prev.left and not prev.right):
                if s == targetSum:
                    return True
                else:
                    return False
            if not node:
                return False
            
            left = recur(s+node.val, node.left, node)
            right = recur(s+node.val, node.right, node)
            return  left or right
            
        return recur(0, root, root)
        # return True
                