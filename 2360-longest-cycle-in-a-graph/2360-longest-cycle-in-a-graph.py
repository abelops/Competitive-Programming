class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        deg = defaultdict(int)
        leng = len(edges)
        visited = [False] * leng
        for i in range(leng):
            deg[edges[i]]+=1
        ans = -1
        
        q = deque()
        for i in range(leng):
            if deg[i] == 0:
                q.append(i)
        stat = True
        while q:
            poped = q.popleft()
            visited[poped] = True
            if edges[poped] != -1:
                deg[edges[poped]]-=1
            if not deg[edges[poped]]:
                q.append(edges[poped])
        for i in range(leng):
            if not visited[i]:
                c = 1
                visited[i] = True
                temp = edges[i]
                while temp != i:
                    c+=1
                    temp = edges[temp]
                    visited[temp] = True
                ans = max(ans, c)
        return ans