# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, pre: List[int]) -> Optional[TreeNode]:
        st = [TreeNode(float("inf"))]
        for i in pre:
            n = TreeNode(i)
            if st[-1].val > i:
                st[-1].left = n
            else:
                while st[-1].val < i:
                    val = st.pop()
                val.right = n
            st.append(n)
        return st[0].left