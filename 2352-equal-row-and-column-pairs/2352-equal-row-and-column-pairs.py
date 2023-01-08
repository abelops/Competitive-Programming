class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        mp = defaultdict(int)
        colMp = defaultdict(int)
        
        col = [ [str(x)+","] for x in grid[0]]
        
        for i in range(len(grid)):
            r = ""
            for j in range(len(grid[i])):
                r+=str(grid[i][j])+","
                if i > 0:
                    col[j].append(str(grid[i][j])+",")
            mp[r]+=1
        
        for i in col:
            colMp["".join(i)]+=1
        
        fin = 0
        for i in mp:
            if i in colMp:
                fin+= mp[i] * colMp[i]
            
        print(mp, colMp)
        return fin
                
                
            
                