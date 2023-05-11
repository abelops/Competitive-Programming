class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        degree = defaultdict(int)
        graph = defaultdict(list)
        ans = [set() for x in range(n)]
        
        for start, end in edges:
            graph[start].append(end)
            degree[end]+=1
        q = deque()
        
        for i in range(n):
            if not degree[i]:
                q.append(i)
        while q:
            poped = q.popleft()
            for i in graph[poped]:
                ans[i].add(poped)
                ans[i] = ans[i].union(ans[poped])
                degree[i]-=1
                if degree[i] == 0:
                    q.append(i)
        return [sorted(x) for x in ans]