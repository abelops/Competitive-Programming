class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        ans = 1
        mp = defaultdict(list)
        for i in range(len(parent)):
            if i not in mp:
                mp[i] = []
            if parent[i] != -1:
                mp[parent[i]].append(i)
        # print(mp)
        def dfs(num):
            nonlocal ans
            if not mp[num]:
                return [s[num], 1]
            arr = []
            for i in mp[num]:
                ret = dfs(i)
                if ret and ret[0] != s[num]:
                    ret[0] = s[num]
                    ret[1]+=1
                    arr.append(ret)
            arr = sorted(arr, key=lambda x: x[1])
            # print(num,arr)
            if len(arr) > 1:
                ans = max(ans, arr[-2][1] + arr[-1][1] -1)
            elif len(arr) == 1:
                ans = max(ans, arr[0][1])
            if not arr:
                return [s[num], 1]
            return arr[-1]
        dfs(0)
        # print(ans)
        return ans
            
            