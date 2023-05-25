class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for c, (i, j) in enumerate(costs):
            diff.append([j-i, c])
        diff = sorted(diff)
        ans = 0
        for i in range(len(costs)//2):
            ans+=costs[diff[i][1]][1]
        for i in range(len(costs)//2, len(costs)):
            ans+=costs[diff[i][1]][0]
        return ans
    
            