class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = -1
        neg = 0
        prev = 0
        l = len(gas)
        for i in range(l):
            prev += gas[i]
            prev -= cost[i]
            if prev < 0:
                neg-=prev
                prev = 0
                idx = -1
            else:
                if idx == -1:
                    idx = i
        if prev - neg >= 0:
            return idx
        return -1