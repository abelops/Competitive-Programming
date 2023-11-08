class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        tot = 1
        for start, end in tickets[::-1]:
            graph[start].append(end)
            tot+=1
        ans = []
        def dfs(cur, c):
            nonlocal ans
            if c == tot:
                return
            while graph[cur]:
                poped = graph[cur].pop()
                dfs(poped, c+1)
            ans.append(cur)
        dfs("JFK", 0)
        return ans[::-1]
            
    