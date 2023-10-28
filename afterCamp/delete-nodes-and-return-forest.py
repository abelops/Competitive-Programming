# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        toDel = set(to_delete)
        def dfs(cur):
            nonlocal ans
            if not cur:
                return TreeNode(None)
            left = dfs(cur.left)
            right = dfs(cur.right)
            if cur.val in toDel:
                if left.val:
                    ans.append(left)
                if right.val:
                    ans.append(right)
                return TreeNode(None)
            ret = TreeNode(cur.val)
            if left.val:
                ret.left = left
            if right.val:
                ret.right = right
            return ret
        ret = dfs(root)
        if ret.val:
            ans.append(ret)
        return ans
                