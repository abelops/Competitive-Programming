class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d = "r"
        ans = []
        
        row, col = len(matrix), len(matrix[0])
        
        tl, tr = 0, col-1
        bl, br = 0, row - 1
        
        i, j = 0, 0
        
        while True:
            if len(ans) == row*col:
                return ans
            if d == "r":
                if j <= tr:
                    ans.append(matrix[i][j])
                    j+=1
                else:
                    tr-=1
                    i+=1
                    j-=1
                    d = "b"
            elif d == "b":
                if i <= br:
                    ans.append(matrix[i][j])
                    i+=1
                else:
                    br-=1
                    j-=1
                    i-=1
                    d = "l"
            elif d == "l":
                if j >= bl:
                    ans.append(matrix[i][j])
                    j-=1
                else:
                    bl+=1
                    j+=1
                    i-=1
                    d = "t"
            elif d == "t":
                if i > tl:
                    ans.append(matrix[i][j])
                    i-=1
                else:
                    tl+=1
                    i+=1
                    j+=1
                    d="r"
            
            
        return ans