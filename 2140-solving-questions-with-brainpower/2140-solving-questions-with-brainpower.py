class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        leng = len(questions)
        memo = {}
        def dp(tot, i):
            nonlocal memo
            if i >= leng:
                return tot
            if (tot, i) in memo:
                return memo[(tot,i)]
            left = dp(tot, i + questions[i][1]+1)+questions[i][0]
            right = dp(tot, i+1)
            memo[(tot, i)] = max(left, right)
            return memo[(tot, i)]
        return dp(0, 0)