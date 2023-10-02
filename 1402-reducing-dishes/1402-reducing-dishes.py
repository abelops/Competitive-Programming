class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sat = sorted(satisfaction)
        leng = len(satisfaction)
        ans = [0] * leng
        for i in range(leng-1, -1, -1):
            temp = 0
            time = 1
            for j in range(i, leng):
                temp+=sat[j] * time
                time+=1
            ans[i] = temp
        ans = max(ans)
        return ans if ans > 0 else 0