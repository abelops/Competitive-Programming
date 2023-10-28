class Solution:
    def checkMatrix(self,x,y, mat):
        pd = defaultdict(int)
        nd = {}
        col = defaultdict(int)
        row = defaultdict(int)
        
        allSet = set()
        c = 0
        for i in range(y, y+3):
            if i >= len(mat):
                return 0
            for j in range(x, x+3):
                if j >= len(mat[0]):
                    return 0
                if mat[i][j] > 9 or mat[i][j] == 0:
                    return 0
                allSet.add(mat[i][j])
                if i == 0 and j == x+2:     
                    nd[str(i+j)]=mat[i][j]
                else:
                    if str(i+j) in nd:
                        nd[str(i+j)]+=mat[i][j]
                col[str(i)]+=mat[i][j]
                row[str(j)]+=mat[i][j]
            pd[str(0)]+=mat[i][x+c]
            c+=1
        allList = set(list(pd.values())+list(nd.values())+list(col.values())+list(row.values()))
        # print(allList)
        # print(pd,nd,col,row)
        # print("\n")
        if len(allSet) != 9:
            return 0
        if len(allList) == 1:
            return 1
        return 0
                
            
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        tot = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tot+=self.checkMatrix(j,i,grid)
        return tot
        