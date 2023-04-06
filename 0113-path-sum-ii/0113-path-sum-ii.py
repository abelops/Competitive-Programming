# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def recur(values,s,node,prev):
            if not node and (prev and not prev.left and not prev.right):
                if s == targetSum:
                    ans.append(values)
                return
            if not node:
                return
            if not node.left and not node.right:
                left = recur(values[:]+[node.val],s+node.val,node.left, node)
            else:
                left = recur(values[:]+[node.val],s+node.val,node.left, node)
                right = recur(values[:]+[node.val],s+node.val,node.right, node)
            return
        recur([],0,root,root)
        return ans