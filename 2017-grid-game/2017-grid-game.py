class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        def pref(arr):
            for j in range(1,len(arr)):
                arr[j]+=arr[j-1]
            return arr
        r1 = pref(grid[0].copy()[::-1])[::-1]
        r2 = pref(grid[1].copy())
        r1.append(0)
        r2.insert(0,0)
        grid[0] = r1
        grid[1] = r2
        ans = []
        r = 0
        c = 1
        for i in range(1,len(grid[0])):
            ans.append(max(grid[r][c], grid[r+1][c-1]))
            c+=1
        return min(ans)
        
        
        