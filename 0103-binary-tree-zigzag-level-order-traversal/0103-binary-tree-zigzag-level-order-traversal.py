# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]
        q = deque([root])
        d = False
        while q:
            l = len(q)
            temp = []
            for i in range(l):
                poped = q.popleft()
                if poped and poped.left:
                    temp.append(poped.left.val)
                    q.append(poped.left)
                if poped and poped.right:
                    temp.append(poped.right.val)
                    q.append(poped.right)
            if temp:
                if d:
                    ans.append(temp)
                else:
                    ans.append(temp[::-1])
                d = not d
        return ans