# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(cur1, cur2):
            if not cur1 and not cur2:
                return True
            if (cur1 and not cur2) or (not cur1 and cur2) or cur1.val != cur2.val:
                return False
            
            return (dfs(cur1.left, cur2.left) and dfs(cur1.right, cur2.right)) or (dfs(cur1.left, cur2.right) and dfs(cur1.right, cur2.left)) 
            
        return dfs(root1, root2)
                
            
            
            