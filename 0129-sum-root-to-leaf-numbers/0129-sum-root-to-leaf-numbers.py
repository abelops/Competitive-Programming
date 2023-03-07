# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def preOrd(node,val):
            if node:
                if not node.left and not node.right:
                    ans.append(int(val + str(node.val)))
                preOrd(node.left, val+str(node.val))
                preOrd(node.right, val+str(node.val))
            else:
                return
        preOrd(root, "")
        return sum(ans)