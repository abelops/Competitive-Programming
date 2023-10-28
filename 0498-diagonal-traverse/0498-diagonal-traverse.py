class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagMatrix = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                diagMatrix[i+j].append(mat[i][j])
        
        ans = []
        for i in diagMatrix:
            if i%2 == 0:
                odd = list(map(lambda a: a, diagMatrix[i][::-1]))
                ans.extend(odd)
            else:
                even = list(map(lambda a: a,diagMatrix[i]))
                ans.extend(even)
            
        
        return ans
        