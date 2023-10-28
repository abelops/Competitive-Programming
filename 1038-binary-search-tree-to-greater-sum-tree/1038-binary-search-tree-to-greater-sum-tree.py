# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def preOrd(node):
            if not node:
                return []
            return preOrd(node.left) + [node.val] + preOrd(node.right)
        ans = preOrd(root)
        pref = [ans[0]]
        mp = defaultdict(int)
        for i in range(1, len(ans)):
            pref.append(pref[i-1]+ans[i])
        pref = pref[::-1]
        for i in range(len(ans)):
            mp[ans[i]] = pref[0] - pref[-1*i-1] + ans[i]
        def trav(node):
            if not node:
                return
            node.val = mp[node.val]
            trav(node.left)
            trav(node.right)
        trav(root)
        return root