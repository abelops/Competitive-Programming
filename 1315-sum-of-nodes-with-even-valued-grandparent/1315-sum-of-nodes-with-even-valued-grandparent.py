# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        def getChildren(node1, node2):
            nonlocal ans
            if node1:
                if node1.left and node1.right:
                    ans += node1.left.val + node1.right.val
                elif node1.left:
                    ans+= node1.left.val
                elif node1.right:
                    ans+= node1.right.val
            if node2:
                if node2.left and node2.right:
                    ans += node2.left.val + node2.right.val
                elif node2.left:
                    ans+= node2.left.val
                elif node2.right:
                    ans+= node2.right.val 
        def preOrd(node):
            if not node:
                return 
            if node.val % 2 ==0:
                getChildren(node.left, node.right)
            preOrd(node.left)
            preOrd(node.right)
        preOrd(root)
        return ans
            
            