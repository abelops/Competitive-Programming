# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def searchForPos(node, prev):
            if not node:
                if prev.val > val:
                    prev.left = TreeNode(val)
                else:
                    prev.right = TreeNode(val)
                return root
            else:
                if node.val > val:
                    return searchForPos(node.left, node)
                else:
                    return searchForPos(node.right, node)
            return root
        if not root:
            return TreeNode(val)
        return searchForPos(root, root)