class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        deg = defaultdict(int)
        for i, j in edges:
            mp[i].append(j)
            mp[j].append(i)
            deg[j]+=1
            deg[i]+=1
        
        q = deque()
        visited = set()
        c = 0
        for i in range(n):
            if deg[i] == 1:
                q.append(i)
                visited.add(i)
                c+=1
        
        ans = [0]
        while q:
            leng = len(q)
            ans = []
            for i in range(leng):
                poped = q.popleft()
                ans.append(poped)
                for j in mp[poped]:
                    deg[j]-=1
                    if deg[j] == 1 and j not in visited:
                        q.append(j)
                        ans.append(j)
                        visited.add(j)
        return ans