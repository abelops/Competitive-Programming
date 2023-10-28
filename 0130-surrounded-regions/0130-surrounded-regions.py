class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = [[False for x in range(len(board[0]))] for _ in range(len(board))]
        def inBound(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        
        def dfs(i,j):
            nonlocal visited
            visited[i][j] = True
            board[i][j] = "Z"
            for x, y in d:
                dx = x + i
                dy = y + j
                if inBound(dx, dy) and board[dx][dy] == "O" and (dx,dy) not in visited:
                    dfs(dx, dy)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and not visited[i][j]:
                    if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                        # print(board[i][j], visited[i][j])
                        # print(i,j)
                        dfs(i,j)
        # print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "Z":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return board
            
            