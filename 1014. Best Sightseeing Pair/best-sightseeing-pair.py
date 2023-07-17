class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        curMax = values[0]
        for i in range(1, len(values)):
            ans = max(ans, curMax + values[i] - i)
            curMax = max(curMax, i + values[i])
        return ans