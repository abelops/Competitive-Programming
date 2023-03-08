# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:  
        stat = False
        def preOrd(node, check=None):
            nonlocal stat
            if not node:
                return [None]
            ans =  [node.val] +  preOrd(node.left, check) +  preOrd(node.right, check)
            # print(ans, check)
            if check and ans == check:
                stat = True
            return ans
        sub = preOrd(subRoot)
        main =  preOrd(root, sub)
        return stat
            