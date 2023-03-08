# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def getTree(l, r):
            nonlocal nums
            if l > r:
                return 
            mid = l + (r-l)//2
            
            left = getTree(l, mid-1)
            right = getTree(mid+1, r)
            node = TreeNode(nums[mid], left, right)
            
            return node
        ans = getTree(0, len(nums)-1)
        return ans