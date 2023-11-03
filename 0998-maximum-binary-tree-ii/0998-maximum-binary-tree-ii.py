# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def buildArr(cur):
            if not cur:
                return []
            left = buildArr(cur.left)
            right = buildArr(cur.right)
            return left + [cur.val] + right
        arr = buildArr(root)
        arr.append(val)
        
        index = {}
        for i in range(len(arr)):
            index[arr[i]] = i
        def recur(l,r):
            if l == r:
                return None
            maxi = max(arr[l:r])
            idx = index[maxi]
            
            cur = TreeNode(maxi)
            cur.left = recur(l, idx)
            cur.right = recur(idx+1, r)
            return cur
        return recur(0, len(arr))
            
            