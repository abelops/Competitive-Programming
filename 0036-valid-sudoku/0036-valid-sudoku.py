class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowList = [set() for x in range(9)]
        colList = [set() for x in range(9)]
        matrix = [set() for x in range(9)]
        
        r = {0: [1,2,3], 1: [1,2,3], 2: [1,2,3],
             3: [4,5,6], 4: [4,5,6], 5: [4,5,6],
             6: [7,8,9], 7: [7,8,9], 8: [7,8,9]}
        c = {0: [1,4,7], 1: [1,4,7], 2: [1,4,7],
             3: [2,5,8], 4: [2,5,8], 5: [2,5,8],
             6: [3,6,9], 7: [3,6,9], 8: [3,6,9],}
        
        for i in range(len(board)):
            for j in range(len(board[i])): 
                if (board[i][j] in colList[i] and len(colList[i]) > 0) or (board[i][j] in rowList[j] and len(rowList[j]) > 0):
                    return False
                if board[i][j] != ".":
                    rowList[j].add(board[i][j])
                    colList[i].add(board[i][j])
                mat = set(r[i]).intersection(c[j])
                mat = mat.pop()-1
                if len(matrix[mat]) > 0:
                    if board[i][j] in matrix[mat]:
                        return False
                if board[i][j] != ".":
                    matrix[mat].add(board[i][j])
        return True                
        