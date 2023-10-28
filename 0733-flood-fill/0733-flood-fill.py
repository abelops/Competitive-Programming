class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        def isValid(x, y):
            return True if (0 <= x < len(image)) and (0 <= y < len(image[0])) else False
            
        def dfs(visited, x, y):
            visited.append((x,y))
            for i in dirs:
                dx = x + i[0]
                dy = y + i[1]
                if isValid(dx,dy) and tuple([dx,dy]) not in visited:
                    if image[dx][dy] == image[x][y]:
                        dfs(visited, dx, dy)
            image[x][y] = color
                
        dfs([], sr, sc)
        return image
                
            