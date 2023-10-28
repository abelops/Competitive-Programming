# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        max_width = 0
        while q:
            left = q[0][1]
            right = q[-1][1]
            max_width = max(max_width, abs(right - left) + 1)
            
            tq = deque()
            while q:
                node, level = q.pop()
                if node.left:
                    tq.appendleft((node.left, level * 2))
                if node.right:
                    tq.appendleft((node.right, level * 2 + 1))
            q = tq
        return max_width