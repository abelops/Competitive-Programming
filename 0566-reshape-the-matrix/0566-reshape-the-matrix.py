class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flaten = sum(mat, [])
        ans = []
        
        if len(flaten) < r * c:
            return mat
        elif len(flaten) > r * c:
            return mat
        
        ind = 0
        for i in range(r):
            ar = []
            for j in range(c):
                ar.append(flaten[ind])
                ind += 1
            ans.append(ar)
            
        return ans