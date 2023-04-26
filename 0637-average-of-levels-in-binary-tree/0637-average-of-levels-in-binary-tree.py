# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        visited = []
        q = deque([root])
        ans = [root.val]
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
                ans.append(sum(temp)/len(temp))
        return ans
                