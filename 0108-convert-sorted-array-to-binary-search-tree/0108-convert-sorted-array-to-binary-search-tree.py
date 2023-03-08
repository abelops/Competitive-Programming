# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def getTree(l, r):
            if l > r:
                return 
            mid = l + (r-l)//2
            return TreeNode(nums[mid], getTree(l, mid-1), getTree(mid+1, r))
        ans = getTree(0, len(nums)-1)
        return ans