class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        mp = Counter({chr(x): 0 for x in range(97, 123)})
        tree = defaultdict(list)
        ans = [0] * (len(edges)+1)
        visited = set()
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        def dfs(n, par):
            cur = Counter()
            for i in tree[n]:
                if i == par:
                    continue
                ret = dfs(i, n)
                cur+=ret
            cur[labels[n]] += 1
            ans[n] = cur[labels[n]]
            return cur
        dfs(0, None)
        return ans