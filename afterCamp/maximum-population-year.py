class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pref = [0] * 102
        for start, end in logs:
            pref[start-1950+1]+=1
            pref[end-1950+1]-=1
        maxi = (-1,-1)
        for i in range(1,101):
            pref[i]+=pref[i-1]
            if pref[i] > maxi[0]:
                maxi = (pref[i],i)
        # print(pref)
        return maxi[1]+1950-1
        