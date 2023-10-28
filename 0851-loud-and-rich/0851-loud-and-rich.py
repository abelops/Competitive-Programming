class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        mp = defaultdict(list)
        deg = defaultdict(int)
        for big, small in richer:
            mp[big].append(small)
            deg[small]+=1
        ans = [i for i in range(len(quiet))]
        q = deque()
        for i in range(len(quiet)):
            if deg[i] == 0:
                q.append(i)
        while q:
            poped = q.popleft()
            for j in mp[poped]:
                if quiet[ans[poped]] < quiet[ans[j]]:
                    ans[j] = ans[poped]
                deg[j]-=1
                if deg[j] == 0:
                    q.append(j)
        return ans
            