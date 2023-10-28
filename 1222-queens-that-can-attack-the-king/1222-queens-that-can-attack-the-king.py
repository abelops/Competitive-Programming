class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        
        # +x, y 
        for i in range(king[0], 8):
            if [i, king[1]] in queens:
                ans.append([i, king[1]])
                break
        # -x, y
        for i in range(king[0], -1, -1):
            if [i, king[1]] in queens:
                ans.append([i, king[1]])
                break
        # x, +y
        for i in range(king[1], 8):
            if [king[0], i] in queens:
                ans.append([king[0], i])
                break
        # x, -y
        for i in range(king[1], -1, -1):
            if [king[0], i] in queens:
                ans.append([king[0], i])
                break
        # +x, +y
        for i, j in zip(range(king[0], 8), range(king[1], 8)):
            if [i, j] in queens:
                ans.append([i, j])
                break
        # -x, -y
        for i, j in zip(range(king[0], -1, -1), range(king[1], -1, -1)):
            if [i, j] in queens:
                ans.append([i, j])
                break
        # +x, -y
        for i, j in zip(range(king[0], 8), range(king[1], -1, -1)):
            if [i, j] in queens:
                ans.append([i, j])
                break
        # -x, +y
        for i, j in zip(range(king[0], -1, -1), range(king[1], 8)):
            if [i, j] in queens:
                ans.append([i, j])
                break
        return ans
        
                