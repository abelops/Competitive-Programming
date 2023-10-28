"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxDepth = 0 
        def dfs(visited, node, depth):
            nonlocal maxDepth
            if not node:
                return
            maxDepth = max(maxDepth, depth)
            visited.append(node)
            for i in node.children:
                # print(i.val, depth)
                if i not in visited:
                    dfs(visited, i, depth+1)
            
            return
        dfs([], root, 1)
        return maxDepth
                