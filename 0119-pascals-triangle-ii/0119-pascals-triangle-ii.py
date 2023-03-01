class Solution:
    def createPascal(self, lis, cur, dest):
        if cur == dest+1:
            return lis
        ans = []
        for i in range(cur+1):
            if i == 0 or i == cur:
                ans.append(1)
            else:
                ans.append(lis[i-1]+lis[i])
        return self.createPascal(ans, cur+1, dest)
        
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        return self.createPascal([1,1], 2, rowIndex)