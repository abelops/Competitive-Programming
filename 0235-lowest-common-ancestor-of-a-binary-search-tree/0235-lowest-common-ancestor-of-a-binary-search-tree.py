# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        st = [root]
        while st:
            cur = st.pop()
            if cur.val > p.val and cur.val > q.val:
                st.append(cur.left)
            elif cur.val < p.val and cur.val < q.val:
                st.append(cur.right)
            else:
                return cur
        
        