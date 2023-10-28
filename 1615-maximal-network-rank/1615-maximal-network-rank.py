class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        mp = defaultdict(set)
        for i in roads:
            mp[i[0]].add(i[1])
            mp[i[1]].add(i[0])
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                    ch = len(mp[i]) + len(mp[j])
                    if i in mp[j]:
                        ch-=1
                    ans = max(ch, ans)
        return ans