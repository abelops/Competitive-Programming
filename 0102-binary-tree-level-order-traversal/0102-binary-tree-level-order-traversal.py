# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        st = []
        temp = []
        if not root:
            return root
        while q:
            tq = deque()
            while q:
                cur = q.pop()    
                temp.append(cur.val)
                if cur.left:
                    tq.appendleft(cur.left)
                if cur.right:
                    tq.appendleft(cur.right)
            st.append(temp)
            q = tq
            temp = []
        return st

            