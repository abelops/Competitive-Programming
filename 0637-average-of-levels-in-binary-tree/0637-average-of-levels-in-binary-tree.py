# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ans = [root.val]
        while q:
            l = len(q)
            temp = 0
            c = 0
            for i in range(l):
                poped = q.popleft()
                if poped and poped.left:
                    temp+=poped.left.val
                    q.append(poped.left)
                    c+=1
                if poped and poped.right:
                    temp+=poped.right.val
                    q.append(poped.right)
                    c+=1
            if c!=0:
                ans.append(temp/c)
        return ans
                