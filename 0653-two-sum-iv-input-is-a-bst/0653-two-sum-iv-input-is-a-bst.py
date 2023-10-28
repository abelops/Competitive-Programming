# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        mp = {}
        def dfs(cur):
            nonlocal mp
            if k - cur.val in mp:
                print(True)
                return True
            mp[cur.val] = 1
            ret = False
            if cur and cur.left:
                ret = ret or dfs(cur.left)
            if cur and cur.right:
                ret = ret or dfs(cur.right)
            return ret
        ans=dfs(root)
        return ans