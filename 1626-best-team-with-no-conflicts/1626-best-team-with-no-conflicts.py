class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        l = len(scores)
        ageScore = sorted([[ages[x], scores[x]] for x in range(l)])
        ans = [x[1] for x in ageScore]
        for i in range(l-1, -1, -1):
            maxi = 0
            for j in range(i+1, l):
                if ageScore[i][0] < ageScore[j][0] and ageScore[i][1] <= ageScore[j][1]:
                    maxi = max(maxi, ans[j])
                elif ageScore[i][0] == ageScore[j][0]:
                    maxi = max(maxi, ans[j])
            ans[i] += maxi
        print(ageScore)
        return max(ans)