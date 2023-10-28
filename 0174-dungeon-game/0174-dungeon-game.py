class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        for i in range(row):
            dungeon[i].append(float("-inf"))
        dungeon.append([float("-inf")]*(col+1))
        
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                tmp = max(dungeon[i][j+1], dungeon[i+1][j])
                if tmp == float("-inf"):
                    tmp = 0
                if tmp < 0:
                    dungeon[i][j]+= tmp
        return abs(dungeon[0][0])+1 if dungeon[0][0] <= 0 else 1
                    
                        
                        
                    
                    