class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 2:
            ans.append([1,1])
        for i in range(1,numRows-1):
            if i == 1:
                ans.append([1,1])
            temp = [1]
            for i in range(len(ans[-1])-1):
                temp.append(ans[-1][i]+ ans[-1][i+1])
            temp.append(1)
            ans.append(temp)
        
        return ans