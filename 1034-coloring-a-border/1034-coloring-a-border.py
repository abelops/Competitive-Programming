class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        d = [(1,0),(-1,0), (0,1),(0,-1)]
        newGrid = [[x for x in y] for y in grid ]
        def inBound(x,y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        mainColor = grid[row][col]
        
        def dfs(i,j,visited):
            if (i,j) in visited:
                return 0
            neighbourCount = 0
            visited.add((i,j))
            for x, y in d:
                dx = i + x
                dy = j + y
                if inBound(dx,dy) and newGrid[dx][dy] == mainColor:
                    neighbourCount+=1
                    dfs(dx, dy,visited)
            if neighbourCount < 4:
                grid[i][j] = color
            return 0
        dfs(row, col, set())
        return grid
            