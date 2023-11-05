class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = { (x,y):set() for x in range(3) for y in range(3)}
        for i in range(9):
            visitedRow = set()
            visitedCol = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in visitedRow:
                        return False
                    visitedRow.add(board[i][j])
                    row, col = i//3, j//3
                    if board[i][j] in grid[(row,col)]:
                        return False
                    grid[(row,col)].add(board[i][j])
                    
                if board[j][i] != ".":
                    if board[j][i] in visitedCol:
                        return False
                    visitedCol.add(board[j][i])
                    
        return True
                    
              
        
                
                
        
                