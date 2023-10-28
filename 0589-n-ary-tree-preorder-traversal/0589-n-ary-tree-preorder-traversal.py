"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans =[]
        self.dfs(root, ans)
        return ans
    
    def dfs(self, root, ans):
        if root is None:
            return
        ans.append(root.val)
        for child in root.children:
            self.dfs(child, ans)
       