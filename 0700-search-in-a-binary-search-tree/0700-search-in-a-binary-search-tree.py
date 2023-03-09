# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def recur(node):
            if not node:
                return None
            if node.val == val:
                return node
            if node.val > val:
                return recur(node.left)
            else:
                return recur(node.right)
        # Itterative dfs
        def dfs(root):
            st = [root]
            while st:
                cur = st.pop()
                if cur:
                    if cur.val == val:
                        return cur
                    if cur.right:
                        st.append(cur.right)
                    if cur.left:
                        st.append(cur.left)
            return None
                
        return dfs(root)
        # return recur(root) 