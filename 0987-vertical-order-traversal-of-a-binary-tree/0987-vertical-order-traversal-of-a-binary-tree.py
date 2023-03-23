# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(lambda: defaultdict(list))
        def recur(cur,node, y):
            if node:
                mp[cur][y].append(node.val)
            if node.left:
                left = recur(cur+1,node.left, y+1)
            if node.right:
                right = recur(cur-1, node.right, y+1)
            return 
        recur(0, root, 0)
        ans = []
        # print(mp)
        for i in sorted(mp.keys())[::-1]:
            temp = []
            for j in sorted(mp[i]):
                [temp.append(x) for x in sorted(mp[i][j])]
            ans.append(temp)
        return ans