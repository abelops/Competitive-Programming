# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        mp = defaultdict(int)
        
        def trav(cur, s):
            nonlocal ans
            if not cur:
                return
            s+= cur.val
            if s == targetSum:
                ans+=1
            ans+= mp[s-targetSum]
            mp[s] += 1
            trav(cur.left, s)
            trav(cur.right, s)
            mp[s] -= 1
            if mp[s] == 0:
                mp.pop(s)
            return
        trav(root, 0)
        return ans