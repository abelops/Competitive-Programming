# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMax(node):
            if node.right:
                return findMax(node.right)
            return node
        def findMin(node):
            if node.left:
                return findMin(node.left)
            return node
        
        def delete(node, val):
            if not node:
                return node
            if node.val > val:
                node.left = delete(node.left, val)
            elif node.val < val:
                node.right = delete(node.right, val)
            else:
                if not node.left and not node.right:
                    return None
                elif node.left and node.right:
                    pred = findMin(node.right)
                    node.val = pred.val
                    node.right = delete(node.right, pred.val)
                else:
                    temp = node.left if node.left else node.right
                    node = temp
            return node   
        return delete(root, key)