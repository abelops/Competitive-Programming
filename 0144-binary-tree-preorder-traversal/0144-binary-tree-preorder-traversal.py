# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preOrd(rt):
            return [rt.val]+preOrd(rt.left)+preOrd(rt.right) if rt else []
        return preOrd(root)