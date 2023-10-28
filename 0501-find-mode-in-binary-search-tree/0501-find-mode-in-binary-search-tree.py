# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(int)
        def inOrd(node):
            if not node:
                return []
            ans[node.val] += 1
            return inOrd(node.left) + [node.val] + inOrd(node.right)
        inOrd(root)
        fin = []
        m = max(ans.values())
        for i in ans:
            if ans[i] == m:
                fin.append(i)
        return fin
            
            
        
        