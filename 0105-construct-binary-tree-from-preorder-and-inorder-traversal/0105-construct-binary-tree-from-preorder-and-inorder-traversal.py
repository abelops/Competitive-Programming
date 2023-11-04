# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def make(pre, inord):
            if not pre or not inord:
                return None
            node = TreeNode(pre[0])
            pos = inord.index(pre[0])
            node.left = make(pre[1:pos+1], inord[:pos])
            node.right = make(pre[pos+1:], inord[pos+1:])
            return node
            
        return make(preorder, inorder)
        