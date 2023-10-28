# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur) 
        build_graph(root, None)
        ans = []
        def bfs(cur, tot, visited):            
            visited.add(cur)
            if tot == k:
                ans.append(cur)
                return
            for i in graph[cur]:
                if i not in visited:
                    bfs(i, tot+1, visited)
        bfs(target.val, 0, set())
        return ans