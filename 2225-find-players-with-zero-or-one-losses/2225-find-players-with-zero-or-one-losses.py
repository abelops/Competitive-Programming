class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        teams = {}
        for i in matches:
            if i[1] not in teams:
                teams[i[1]] = 1
            else:
                teams[i[1]] += 1
            if i[0] not in teams:
                teams[i[0]] = 0
        oneLost = []
        noLose = []
        for j in teams.items():
            if j[1] == 0:
                noLose.append(j[0])
            elif j[1] == 1:
                oneLost.append(j[0])
        oneLost.sort()
        noLose.sort()
        return [noLose,oneLost]
                