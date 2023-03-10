# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def trav(node):
            nonlocal ans
            if not node:
                return [0, 0] 
            left = trav(node.left)
            right = trav(node.right)
            
            tot = left[0] + right[0] + node.val
            count = left[1] + right[1] + 1
            if tot // count == node.val:
                ans += 1
            return [tot, count]
            
        trav(root)
        return ans
                
            