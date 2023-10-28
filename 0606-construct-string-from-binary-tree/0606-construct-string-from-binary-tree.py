# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preOrd(node, prev):
            if not node:
                if prev and prev.right:
                    # print(prev.right, prev.left)
                    return ["()"]
                else:
                    return []
            return ["("] + [str(node.val)] + preOrd(node.left, node) + preOrd(node.right, node) + [")"] 
        ans = preOrd(root, None)
        # print("".join(ans))
        return "".join(ans[1:-1])