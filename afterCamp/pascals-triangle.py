class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        for i in range(3, numRows+1):
            tmp=[1]
            for j in range(len(ans[-1])-1):
                tmp.append(ans[-1][j]+ans[-1][j+1])
            tmp.append(1)
            ans.append(tmp)
        return ans
            